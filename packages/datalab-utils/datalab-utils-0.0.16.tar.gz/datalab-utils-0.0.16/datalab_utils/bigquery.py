import codecs
import io
import os
import pandas as pd
import tempfile
import uuid

from google.cloud import bigquery, storage


def execute_bq(project_id,
               query,
               destination_project=None,
               destination_dataset=None,
               destination_table=None,
               create_disposition='CREATE_IF_NEEDED',
               write_disposition='WRITE_TRUNCATE'):
    client = bigquery.Client(project=project_id)
    job_config = bigquery.QueryJobConfig()
    job_config.use_legacy_sql = False

    if destination_dataset and destination_table:
        dataset_ref = client.dataset(destination_dataset, project=destination_project or project_id)
        table_ref = dataset_ref.table(destination_table)
        job_config.destination = table_ref
        job_config.create_disposition = create_disposition
        job_config.write_disposition = write_disposition

    job = client.query(query, job_config=job_config)
    job.result()


def to_gbq(df,
           project_id,
           dataset_id,
           table_id,
           write_disposition='WRITE_EMPTY',
           create_disposition='CREATE_IF_NEEDED'):
    if df.empty:
        print('DataFrame is empty, skipping load')
        return
    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset_id, project=project_id)
    table_ref = dataset_ref.table(table_id)

    print('Loading DataFrame to %s' % table_ref)
    temporary_local_file = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()) + '.csv')
    try:
        print('Creating temporary %s' % temporary_local_file)
        df.to_csv(temporary_local_file, index=False, encoding='utf-8')
        rb_file = codecs.open(temporary_local_file, 'rb', encoding='utf-8')
        print('Loading temporary csv to %s' % table_ref)
        job_config = bigquery.LoadJobConfig()
        job_config.encoding = 'UTF-8'
        job_config.source_format = 'CSV'
        job_config.write_disposition = write_disposition
        job_config.create_disposition = create_disposition
        job_config.schema = _get_bq_schema(df)
        job_config.skip_leading_rows = 1
        job = client.load_table_from_file(rb_file, table_ref, job_config=job_config)
        job.result()
        print('DataFrame loaded to %s' % table_ref)
    finally:
        os.remove(temporary_local_file)


def read_gbq(
        query,
        project_id,
        use_legacy_sql=False):
    job_config = bigquery.QueryJobConfig()
    job_config.flatten_results = True
    job_config.use_legacy_sql = use_legacy_sql

    print('Executing %s' % query)
    client = bigquery.Client(project=project_id)
    job = client.query(query, job_config)
    results = job.result()

    print('Fetching results')
    rows = list(results)
    fields = [field.to_api_repr() for field in results.schema]
    columns = [field['name'] for field in fields]
    return pd.DataFrame.from_records(rows, columns=columns)


def read_gbq_table(
        project_id,
        dataset_id,
        table_id,
        temporary_bucket_name='temporary_work',
        facturation_project_id=None,
        tqdm=None):
    work_directory = _extract_bq_table(project_id, dataset_id, table_id, temporary_bucket_name, facturation_project_id)
    dtype = _table_dtypes(project_id, dataset_id, table_id)
    df = _load_from_storage(project_id, temporary_bucket_name, work_directory, dtype, tqdm)
    _delete_bucket_data(project_id, temporary_bucket_name, work_directory)
    return df


def _extract_bq_table(project_id, dataset_id, table_id, bucket_name, facturation_project_id):
    work_directory = str(uuid.uuid4())
    facturation_project_id = facturation_project_id or project_id

    # Prepare extract job
    client = bigquery.Client(project=facturation_project_id)
    dataset_ref = client.dataset(dataset_id, project=project_id)
    table_ref = dataset_ref.table(table_id)
    gs_uri = "gs://{}/{}/part_*.csv.gz".format(bucket_name, work_directory)
    extract_conf = bigquery.ExtractJobConfig()
    extract_conf.compression = 'GZIP'
    extract_conf.destination_format = 'CSV'

    # Ensure bucket exists
    location = client.get_dataset(dataset_ref).location
    _ensure_bucket(project_id, bucket_name, location)

    print('Extracting table %s to %s' % (table_ref, gs_uri))
    extract_job = client.extract_table(table_ref, gs_uri, job_config=extract_conf)
    extract_job.result()
    return work_directory


def _table_dtypes(project_id, dataset_id, table_id):
    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset_id, project=project_id)
    table_ref = dataset_ref.table(table_id)
    dtype_map = {'STRING': 'str', 'INTEGER': 'float64', 'FLOAT': 'float64', 'BOOLEAN': 'bool', 'TIMESTAMP': 'M8[ns]', 'RECORD': 'object'}
    return {
        field.name: dtype_map[field.field_type]
        for field in client.get_table(table_ref).schema
    }


def _load_part(blob, dtype):
    content = blob.download_as_string()
    return pd.read_csv(io.BytesIO(content), dtype=dtype, compression='gzip')


def _load_from_storage(project_id, bucket_name, work_directory, dtype, tqdm):
    client = storage.client.Client(project=project_id)
    bucket = storage.bucket.Bucket(client, bucket_name)
    parts = list(bucket.list_blobs(prefix=work_directory + "/"))
    parts = tqdm(parts) if tqdm else parts
    raw_data = []
    print('Loading %s files from gs://%s/%s' % (len(parts), bucket_name, work_directory))
    for part in parts:
        df = _load_part(part, dtype)
        raw_data.append(df)
    return pd.concat(raw_data)


def _ensure_bucket(project_id, bucket_name, location):
    client = storage.client.Client(project=project_id)
    bucket = storage.bucket.Bucket(client, bucket_name)
    bucket.location = location
    if not bucket.exists():
        print('Creating bucket gs://%s (location: %s)' % (bucket_name, location))
        bucket.create()
    return bucket


def _delete_bucket_data(project_id, bucket_name, work_directory):
    client = storage.client.Client(project=project_id)
    bucket = storage.bucket.Bucket(client, bucket_name)
    blobs = list(bucket.list_blobs(prefix=work_directory + "/"))

    print('Deleting %s files in gs://%s/%s' % (len(blobs), bucket_name, work_directory))
    bucket.delete_blobs(blobs)


def _get_bq_schema(df):
    BQ_TYPES = {
        'i': 'INTEGER',
        'b': 'BOOLEAN',
        'f': 'FLOAT',
        'O': 'STRING',
        'S': 'STRING',
        'U': 'STRING',
        'M': 'TIMESTAMP'
    }
    return [
        bigquery.SchemaField(column_name, BQ_TYPES.get(dtype.kind, 'STRING'))
        for column_name, dtype in df.dtypes.iteritems()
    ]




import json
import pandas as pd
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/etc/efficiency-api-service.gcskey.json'

project_id = 'efficiencyai-sarenza-data'
dataset_id = 'project_26'

factors = [
    ['mailing', json.dumps({"name": "Mailing", "type": "linear", "b": 1.0, "a": 0.000001, "target_name": "Increase (%)", "max_value": 1000000, "value_name": "Mails", "min_value": 0})],
    ['weather', json.dumps({"name": "Weather", "type": "category", "values": {"cloudy": 70, "fog": 60, "sun": 120, "rain": 90}, "value_name": "Weather Type", "target_name": "Increase (%)"})]
]
factors = pd.DataFrame(factors, columns=['factor_id', 'config'])
to_gbq(factors, project_id, dataset_id, "traffic_factors", write_disposition="WRITE_TRUNCATE")
