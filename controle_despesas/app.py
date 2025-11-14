from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from forms import LancamentoForm, FiltroForm
from datetime import date
from config import Config  # 👈 importa a classe Config

app = Flask(__name__)
app.config.from_object(Config)  # 👈 carrega as configurações do config.py

# 🔹 INICIALIZA O BANCO
db = SQLAlchemy(app)


# 🔹 MODELO DO BANCO DE DADOS
class Lancamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False)  # Receita ou Despesa
    descricao = db.Column(db.String(120), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    data = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Lancamento {self.descricao} ({self.tipo})>"

# 🔹 ROTA PRINCIPAL
@app.route('/', methods=['GET', 'POST'])
def index():
    form = LancamentoForm()
    filtro_form = FiltroForm()

    # ➕ Adiciona lançamento (Receita ou Despesa)
    if form.validate_on_submit():
        novo = Lancamento(
            tipo=form.tipo.data,
            descricao=form.descricao.data,
            valor=float(form.valor.data),
            categoria=form.categoria.data,
            data=form.data.data
        )
        db.session.add(novo)
        db.session.commit()
        flash(f"{novo.tipo} '{novo.descricao}' adicionada com sucesso!", 'success')
        return redirect(url_for('index'))

    # 🔍 Filtragem
    query = Lancamento.query

    if filtro_form.validate_on_submit():
        if filtro_form.tipo.data:
            query = query.filter_by(tipo=filtro_form.tipo.data)
        if filtro_form.categoria.data:
            query = query.filter_by(categoria=filtro_form.categoria.data)
        if filtro_form.data_inicio.data:
            query = query.filter(Lancamento.data >= filtro_form.data_inicio.data)
        if filtro_form.data_fim.data:
            query = query.filter(Lancamento.data <= filtro_form.data_fim.data)

    lancamentos = query.order_by(Lancamento.data.desc()).all()

    # 💰 Calcula saldo total (Receitas - Despesas)
    saldo = sum(l.valor if l.tipo == 'Receita' else -l.valor for l in lancamentos)

    return render_template(
        'index.html',
        form=form,
        filtro_form=filtro_form,
        lancamentos=lancamentos,
        saldo=saldo
    )

# 🔹 CRIA AS TABELAS AUTOMATICAMENTE (caso não existam)
with app.app_context():
    db.create_all()

# 🔹 EXECUTA O SERVIDOR FLASK
if __name__ == '__main__':
    app.run(debug=True)
