# include the database congifurations

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'mysecretkey'

class ProductionConfig(Config):
    # include the database configurations for POSTGRES
    POSTGRES_USER = 'postgres'
    POSTGRES_PW = 'postgres'
    POSTGRES_URL = 'localhost:5432'
    POSTGRES_DB = 'example'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}'


class DevelopmentConfig(Config):
    POSTGRES_USER = 'postgres'
    POSTGRES_PW = 'postgres'
    POSTGRES_URL = 'localhost:5432'
    POSTGRES_DB = 'example'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}'
    
    DEBUG = True

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    TESTING = True
