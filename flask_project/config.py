import os
from boto.s3.connection import S3Connection

s3 = S3Connection(os.environ['SECRET_KEY'], os.environ['MAIL_PASSWORD'])

SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = "example@gmail.com"
