from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

CATEGORIAS = [
    'Despesas Fixas', 'Funcionarios', 'Insumos', 'Limpeza', 'Aluguel',
    'Investimentos', 'Taxas e Tarifas', 'Pro Labore', 'Imposto de Renda',
    'Contabilidade', 'Energia Eletrica', 'Diaristas', 'Manutenção Predial'
]

class LancamentoForm(FlaskForm):
    tipo = SelectField('Tipo', choices=[
        ('Despesa', 'Despesa'),
        ('Receita', 'Receita')
    ], validators=[DataRequired()])
    
    descricao = StringField('Descrição', validators=[DataRequired(), Length(min=3, max=120)])
    valor = DecimalField('Valor (R$)', validators=[DataRequired(), NumberRange(min=0)])
    categoria = SelectField('Categoria', choices=[(c, c) for c in CATEGORIAS])
    data = DateField('Data', validators=[DataRequired()])
    submit = SubmitField('Salvar')

class FiltroForm(FlaskForm):
    tipo = SelectField('Tipo', choices=[
        ('', 'Todos'),
        ('Despesa', 'Despesa'),
        ('Receita', 'Receita')
    ], validators=[Optional()])
    
    categoria = SelectField('Categoria', choices=[('', 'Todas')] + [(c, c) for c in CATEGORIAS], validators=[Optional()])
    
    data_inicio = DateField('De', validators=[Optional()])
    data_fim = DateField('Até', validators=[Optional()])
    submit = SubmitField('Filtrar')
