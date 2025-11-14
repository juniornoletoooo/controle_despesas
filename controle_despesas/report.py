import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def gerar_relatorio(despesas):
    pasta = "relatorios"
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    nome_arquivo = f"relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    caminho = os.path.join(pasta, nome_arquivo)

    c = canvas.Canvas(caminho, pagesize=A4)
    largura, altura = A4
    c.setTitle("Relatório de Despesas")

    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, altura - 50, "Relatório de Despesas")
    c.setFont("Helvetica", 10)
    c.drawString(50, altura - 70, f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

    y = altura - 100
    total = 0

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Descrição")
    c.drawString(250, y, "Categoria")
    c.drawString(380, y, "Data")
    c.drawString(460, y, "Valor (R$)")
    y -= 20

    c.setFont("Helvetica", 10)
    for despesa in despesas:
        c.drawString(50, y, despesa.descricao[:25])
        c.drawString(250, y, despesa.categoria)
        c.drawString(380, y, despesa.data.strftime('%d/%m/%Y'))
        c.drawString(460, y, f"{despesa.valor:.2f}")
        total += despesa.valor
        y -= 15
        if y < 50:
            c.showPage()
            y = altura - 50

    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, f"Total geral: R$ {total:.2f}")

    c.save()
    return caminho
