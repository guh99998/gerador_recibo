from docx import Document
from docx.shared import Inches
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import RGBColor

nome_recibo = "teste"#input('Digite o nome do recibo criado: ')#
nome_cliente = "nome_cliente"#input
valor_recibo = "valor_recibo"#input
cpf_cliente = "cpf_cliente"#input e opcional
referencia_recibo = "referencia recibo (colocar o texto que vai após 'referente a ...')"#input
data_recibo = "data_recibo"#input
local_recibo = "local_recibo"#input
recebedor = "recebedor"#input
doc_recebedor = "documento recebedor"#input

document = Document()

titulo = document.add_heading('RECIBO', level=0)
titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER

valor = document.add_paragraph()
run_valor = valor.add_run(f'R${valor_recibo}')
run_valor.font.size = Pt(16)
valor.alignment = WD_ALIGN_PARAGRAPH.RIGHT

corpo = document.add_paragraph()
run_corpo = corpo.add_run('''

''')

document.save(f'{nome_recibo}.docx')