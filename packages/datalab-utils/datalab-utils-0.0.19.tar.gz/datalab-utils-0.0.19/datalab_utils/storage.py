import io
import fnmatch
import pandas as pd

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
from google.cloud import storage


def read_gs_csv(project_id, uri, **kwargs):
    print('Loading %s in memory' % uri)
    buffer = io.BytesIO()
    for blob in _list_blobs(project_id, uri):
        blob.download_to_file(buffer)
    buffer.seek(0)
    print('Loading DataFrame')
    df = pd.read_csv(buffer, **kwargs)
    del buffer
    return df


def _list_blobs(project_id, uri):
    parts = urlparse(uri)
    bucket_name = parts.netloc
    blob_pattern = parts.path
    if blob_pattern.startswith('/'):
        blob_pattern = blob_pattern[1:]

    client = storage.client.Client(project=project_id)
    bucket = storage.bucket.Bucket(client, bucket_name)
    assert bucket, 'Bucket %s not found' % bucket_name
    blobs = [blob for blob in bucket.list_blobs() if fnmatch.fnmatch(blob.name, blob_pattern)]
    assert blobs, 'No blob found for %s' % uri

    return blobs
