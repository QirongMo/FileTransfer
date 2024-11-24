
## FTPTransfer.py
from .DataTransferBase import DataTransferBase
from ftplib import FTP


class FTPTransfer(DataTransferBase):

    def __init__(self, **kwargs):
        self.ftp = None
        self.ftp_ip, self.ftp_port, self.ftp_user, self.ftp_pwd, self.ftp_dir = kwargs.get("ftp_ip"), \
            kwargs.get("ftp_port"), kwargs.get("ftp_user"), kwargs.get("ftp_pwd"), kwargs.get("ftp_dir")
        
    def connect(self):
        if self.ftp is None:
            self.ftp = FTP()
            self.ftp.connect(self.ftp_ip, self.ftp_port)
            self.ftp.login(self.ftp_user, self.ftp_pwd)
            self.ftp.encoding = "GB18030"
            if self.ftp_dir:
                self.ftp.cwd(self.ftp_dir)

    def download(self, url_path, local_path):
        self.connect()
        with open(local_path, 'wb') as fp:
            self.ftp.retrbinary('RETR ' + url_path, fp.write)

    def upload(self, local_path, save_path):
        self.connect()
        with open(local_path, 'rb') as fp:
            self.ftp.storbinary('STOR ' + save_path, fp)

    def close(self):
        self.ftp.quit()
        self.ftp = None
    
    def get_object(self, url_path) -> bytes:
        self.connect()
        data_bytes = b""
        def handle_binary(more_data):
            nonlocal data_bytes
            data_bytes += more_data
        self.ftp.retrbinary(f"RETR {url_path}", callback=handle_binary)
        return data_bytes
