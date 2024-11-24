
## OSSTransfer.py
from .DataTransferBase import DataTransferBase
import oss2


class OSSTransfer(DataTransferBase):

    def __init__(self, **kwargs):
        self.oss_bucket = None
        self.oss_accessKeyId, self.oss_accessKeySecret, self.oss_endPoint, self.oss_bucketName = \
            kwargs.get("oss_accessKeyId"), kwargs.get("oss_accessKeySecret"), \
            kwargs.get("oss_endPoint"), kwargs.get("oss_bucketName")

    def connect(self):
        if self.oss_bucket is None:
            auth = oss2.Auth(self.oss_accessKeyId, self.oss_accessKeySecret)
            self.oss_bucket = oss2.Bucket(auth, 'http://' + self.oss_endPoint,
                                          self.oss_bucketName)

    def download(self, url_path, local_path):
        self.connect()
        self.oss_bucket.get_object_to_file(url_path, local_path)

    def upload(self, local_path, save_path):
        self.connect()
        self.oss_bucket.put_object(save_path, local_path)

    def close(self):
        self.oss_bucket.close()
        self.oss_bucket = None
    
    def get_object(self, url_path) -> bytes:
        self.connect()
        data_bytes = self.oss_bucket.get_object(url_path).read()
        return data_bytes