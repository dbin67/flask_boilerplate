import os


class Config:
    USER = os.getenv('POSTGRES_USER')
    PASSWORD = os.getenv('POSTGRES_PASSWORD')
    DATABASE = os.getenv('POSTGRES_DB')
    HOST = os.getenv('POSTGRES_HOST')
    PORT = os.getenv('POSTGRES_PORT')

    SQLALCHEMY_DATABASE_URI = \
        f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
