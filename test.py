
from FileTransfer import FileTransfer, DataTransferBase

def test_local():
    ftFun = FileTransfer['local']
    ft: DataTransferBase = ftFun()
    ft.download("requirements.txt", "requirements.txt.bak")

def test_ftp():
    ftFun = FileTransfer['ftp']
    config = {
        "ftp_ip": "192.168.8.2",
        "ftp_port": 21,
        "ftp_user": "",
        "ftp_pwd": "",
        "ftp_dir": "",
    }
    ft: DataTransferBase = ftFun(**config)
    ft.download("requirements.txt", "requirements.txt.bak")

def test_http():
    ftFun = FileTransfer['http']
    config = {}
    ft: DataTransferBase = ftFun(**config)
    ft.download("https://imgslim.geekpark.net/uploads/image/file/3f/c7/3fc7528e4b81f385cc039c85ec0533da.jpg", "baidu.jpg")


def test_minio():
    ftFun = FileTransfer['minio']
    config = {
        "minio_endpoint": "192.168.8.2:9000",
        "minio_bucket_name": "桶名",
        "minio_access_key": "账号",
        "minio_secret_key": "密码",
    }
    ft: DataTransferBase = ftFun(**config)
    ft.download("requirements.txt", "requirements.txt.bak")


def test_obs():
    ftFun = FileTransfer['obs']
    config = {
        "obs_server": "192.168.8.2:9000",
        "obs_bucket_name": "桶名",
        "obs_access_key_id": "账号",
        "obs_secret_access_key": "密码",
    }
    ft: DataTransferBase = ftFun(**config)
    ft.download("requirements.txt", "requirements.txt.bak")


def test_oss():
    ftFun = FileTransfer['oss']
    config = {
        "oss_endPoint": "192.168.8.2:9000",
        "oss_bucketName": "桶名",
        "oss_accessKeyId": "账号",
        "oss_accessKeySecret": "密码",
    }
    ft: DataTransferBase = ftFun(**config)
    ft.download("requirements.txt", "requirements.txt.bak")

if __name__ == "__main__":
    test_http()

