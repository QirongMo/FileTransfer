
## LocalTransfer.py

from .DataTransferBase import DataTransferBase
import shutil


class LocalTransfer(DataTransferBase):

    def get_object(self, url_path) -> bytes:
        with open(url_path, "rb") as f:
            data_bytes = f.read()
        return data_bytes

    def download(self, url_path, local_path):
        shutil.copy2(url_path, local_path)

    def upload(self, local_path, save_path):
        shutil.copy2(local_path, save_path)
