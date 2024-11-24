

from .DataTransferBase import DataTransferBase
from .LocalTransfer import LocalTransfer
from .FTPTransfer import FTPTransfer
from .HTTPTransfer import HTTPTransfer
from .MinioTransfer import MinioTransfer
from .OBSTransfer import OBSTransfer
from .OSSTransfer import OSSTransfer

__all__ = ["FileTransfer", "DataTransferBase"]

FileTransfer = {
    "local": LocalTransfer,
    "ftp": FTPTransfer,
    "http": HTTPTransfer,
    "minio": MinioTransfer,
    "obs": OBSTransfer,
    "oss": OSSTransfer,
}

