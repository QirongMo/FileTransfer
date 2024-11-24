
## HTTPTransfer.py
from .DataTransferBase import DataTransferBase
import requests


class HTTPTransfer(DataTransferBase):

    def download(self, url_path, local_path):
        data_bytes = self.get_object(url_path)
        with open(local_path, 'wb') as f:
            f.write(data_bytes)
            
    def get_object(self, url_path) -> bytes:
        url_path = url_path.replace("\\", "/")
        response = requests.get(url_path)
        return response.content