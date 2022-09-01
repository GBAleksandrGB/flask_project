import os
from boto.s3.connection import S3Connection

SQLALCHEMY_DATABASE_URI = S3Connection(os.environ['SQLALCHEMY_DATABASE_URI'])
SQLALCHEMY_TRACK_MODIFICATIONS = S3Connection(os.environ['SQLALCHEMY_TRACK_MODIFICATIONS'])
SECRET_KEY = S3Connection(os.environ['SECRET_KEY'])
MAIL_SERVER = S3Connection(os.environ['MAIL_SERVER'])
MAIL_PORT = S3Connection(os.environ['MAIL_PORT'])
MAIL_USE_TLS = S3Connection(os.environ['MAIL_USE_TLS'])
MAIL_USERNAME = S3Connection(os.environ['MAIL_USERNAME'])
MAIL_PASSWORD = S3Connection(os.environ['MAIL_PASSWORD'])
