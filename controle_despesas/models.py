from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Despesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(120), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(80), nullable=False)
    data = db.Column(db.Date, default=date.today)
