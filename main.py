from docx import Document
from docx.shared import Inches
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import RGBColor
from modules.numero_extenso import number_to_long_number
from modules.format_values import formatar_doc
from modules.format_data import formatar_data

nome_recibo = "Recibo arrendamento de pasto - Adriano"#input('Digite o nome do recibo criado: ')#
nome_cliente = "Adriano Aparecido de Lima"#input str
valor_recibo = 350.00#input float
cpf_cliente = "05410912632"#input e opcional str
referencia_recibo = "pagamento do arrendamento do pasto para colocar gado no Jardim dos Lagos, na cidade Águas de Lindóia - SP. (04 cabeças), referente ao mês de Fevereiro de 2024"#input str
data_recibo = "19/04/2024"#input str
cidade_recibo = "Monte Sião"#input str
estado_recibo = "MG"
recebedor = "Évora Administração de Imóveis ltda"#input str
doc_recebedor = "20024324000177"#input str

document = Document()

titulo = document.add_heading('RECIBO', level=0)
titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER

valor = document.add_paragraph()
run_valor = valor.add_run(f'R${valor_recibo:.2f}')
run_valor.font.size = Pt(20)
valor.alignment = WD_ALIGN_PARAGRAPH.RIGHT
valor.paragraph_format.space_before = Pt(24)
valor.paragraph_format.space_after = Pt(72)

corpo = document.add_paragraph('Recebi de "')
corpo.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
run_corpo = corpo.add_run({nome_cliente.upper()})
run_corpo.bold = True
corpo.add_run(f'", inscrito no CPF n° {formatar_doc(cpf_cliente)}, a importância de R${valor_recibo:.2f} ({number_to_long_number(valor_recibo)}), referente ao {referencia_recibo}.')

data = document.add_paragraph()
data.alignment = WD_ALIGN_PARAGRAPH.CENTER
data_run = data.add_run(f'{cidade_recibo} - {estado_recibo.upper()}, {formatar_data(data_recibo)}.')
data.paragraph_format.space_after = Pt(72)
data.paragraph_format.space_before = Pt(50)

assinatura = document.add_paragraph()
assinatura.add_run('\n\n')
assinatura.add_run('__________________________________________________________________________')
assinatura.alignment = WD_ALIGN_PARAGRAPH.CENTER

nome_recebedor = document.add_paragraph()
nome_recebedor.alignment = WD_ALIGN_PARAGRAPH.CENTER
nome_recebedor_run = nome_recebedor.add_run(f'{recebedor.upper()}')
documento_recebedor = document.add_paragraph()
documento_recebedor_run = documento_recebedor.add_run(f'Documento: {formatar_doc(doc_recebedor)}')
documento_recebedor.alignment = WD_ALIGN_PARAGRAPH.CENTER

document.save(f'{nome_recibo}.docx')