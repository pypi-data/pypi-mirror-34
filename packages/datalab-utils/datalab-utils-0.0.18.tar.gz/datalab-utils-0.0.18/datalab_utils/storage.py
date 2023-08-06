import io
import pandas as pd

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse
from google.cloud import storage


def read_gs_csv(project_id, uri, **kwargs):
    parts = urlparse(uri)
    bucket_name = parts.netloc
    blob_name = parts.path
    if blob_name.startswith('/'):
        blob_name = blob_name[1:]

    client = storage.client.Client(project=project_id)
    bucket = storage.bucket.Bucket(client, bucket_name)
    assert bucket, 'Bucket %s not found' % bucket_name
    blob = bucket.get_blob(blob_name)
    assert blob, 'Blob %s not found' % uri

    print('Loading %s in memory' % uri)
    buffer = io.BytesIO()
    blob.download_to_file(buffer)
    buffer.seek(0)
    print('Loading DataFrame')
    df = pd.read_csv(buffer, **kwargs)
    del buffer
    return df