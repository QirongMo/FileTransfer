
## OBSTransfer.py
from .DataTransferBase import DataTransferBase
from obs import ObsClient


class OBSTransfer(DataTransferBase):

    def __init__(self, **kwargs):
        self.obs_client = None
        self.obs_access_key_id, self.obs_bucket_name, self.obs_secret_access_key, self.obs_server = \
            kwargs.get("obs_access_key_id"), kwargs.get("obs_bucket_name"), \
            kwargs.get("obs_secret_access_key"), kwargs.get("obs_server")

    def connect(self):
        if self.obs_client is None:
            self.obs_client = ObsClient(
                access_key_id=self.obs_access_key_id,
                secret_access_key=self.obs_secret_access_key,
                server=self.obs_server
            )

    def download(self, url_path, local_path):
        self.connect()
        self.obs_client.getObject(self.obs_bucket_name, objectKey=url_path, downloadPath=local_path)

    def upload(self, local_path, save_path):
        self.connect()
        self.obs_client.putFile(self.obs_bucket_name, save_path, local_path)

    def close(self):
        self.obs_client = None
    
    def get_object(self, url_path) -> bytes:
        self.connect()
        response = self.obs_client.getObject(self.obs_bucket_name, url_path)
        return response.body.read()
