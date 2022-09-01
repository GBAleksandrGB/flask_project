import os
from boto.s3.connection import S3Connection

s3 = S3Connection(os.environ['MAIL_PASSWORD'], os.environ['SECRET_KEY'])

SECRET_KEY = s3.secret_key
SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = "example@gmail.com"
MAIL_PASSWORD = s3.access_key
