
## MinioTransfer.py
from .DataTransferBase import DataTransferBase
from minio import Minio


class MinioTransfer(DataTransferBase):

    def __init__(self, **kwargs):
        self.minio_client = None
        self.minio_endpoint, self.minio_bucket_name, self.minio_access_key, self.minio_secret_key = \
            kwargs.get("minio_endpoint"), kwargs.get("minio_bucket_name"), \
            kwargs.get("minio_access_key"), kwargs.get("minio_secret_key")

    def connect(self):
        if self.minio_client is None:
            self.minio_client = Minio(self.minio_endpoint,
                                      access_key=self.minio_access_key,
                                      secret_key=self.minio_secret_key,
                                      secure=False)

    def download(self, url_path, local_path):
        self.connect()
        self.minio_client.fget_object(self.minio_bucket_name, url_path, local_path)

    def upload(self, local_path, save_path):
        self.connect()
        self.minio_client.fput_object(self.minio_bucket_name, save_path, local_path)

    def close(self):
        self.minio_client = None
    
    def get_object(self, url_path) -> bytes:
        self.connect()
        response = self.minio_client.get_object(self.minio_bucket_name, url_path)
        return response.read()
    
