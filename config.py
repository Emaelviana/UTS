import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ceritanya-ini-secret-kode'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:root@localhost/sesi2'
    SQLALCHEMY_TRACK_MODIFICATIONS=False