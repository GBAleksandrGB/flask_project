import os
from boto.s3.connection import S3Connection


SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = S3Connection(os.environ['SECRET_KEY'])
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = "tomilov.alex@gmail.com"
MAIL_PASSWORD = S3Connection(os.environ['MAIL_PASSWORD'])
