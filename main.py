from docx import Document
from docx.shared import Inches
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import RGBColor
from modules.numero_extenso import number_to_long_number
from modules.format_values import formatar_doc

nome_recibo = "Recibo arrendamento de pasto - Adriano"#input('Digite o nome do recibo criado: ')#
nome_cliente = "Adriano Aparecido de Lima"#input str
valor_recibo = 350.00#input float
cpf_cliente = "05410912632"#input e opcional str
referencia_recibo = "pagamento do arrendamento do pasto para colocar gado no Jardim dos Lagos, na cidade Águas de Lindóia - SP. (04 cabeças), referente ao mês de Fevereiro de 2024"#input str
data_recibo = "19/04/2024"#input str
cidade_recibo = "Monte Sião"#input str
estado_recibo = "MG"
recebedor = "recebedor"#input str
doc_recebedor = "documento recebedor"#input str

document = Document()

titulo = document.add_heading('RECIBO', level=0)
titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER

valor = document.add_paragraph()
run_valor = valor.add_run(f'R${valor_recibo}')
run_valor.font.size = Pt(16)
valor.alignment = WD_ALIGN_PARAGRAPH.RIGHT

corpo = document.add_paragraph('Recebi de "')
corpo.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
run_corpo = corpo.add_run({nome_cliente.upper()})
run_corpo.bold = True
corpo.add_run(f'", inscrito no CPF n° {formatar_doc(cpf_cliente)}, a importância de R${valor_recibo:.2f} ({number_to_long_number(valor_recibo)}), referente ao {referencia_recibo}.')


document.save(f'{nome_recibo}.docx')