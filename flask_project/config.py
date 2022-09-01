import os
from boto.s3.connection import S3Connection


key_1 = S3Connection(os.environ['SECRET_KEY'])
key_2 = S3Connection(os.environ['MAIL_PASSWORD'])

SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key_1
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = "example@gmail.com"
MAIL_PASSWORD = key_2
