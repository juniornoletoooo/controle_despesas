import os

class Config:
    SECRET_KEY = 'minha-chave-secreta-supersegura'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:208395@localhost:5432'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
