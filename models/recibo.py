from docx import Document
from docx.shared import Pt
from modules.format_documento import formatar_doc
from modules.format_data import formatar_data
from modules.format_numero_extenso import formatar_numero_extenso
from constants import *

class Recibo:
    def __init__(self, pagador, recebedor, nome, valor, referencia, data, cidade, estado):
        self.document = Document()
        self._pagador = pagador
        self._recebedor = recebedor
        self._nome = nome
        self._valor = valor
        self._referencia = referencia
        self._data = data
        self._cidade = cidade
        self._estado = estado

    def add_titulo(self):
        titulo = self.document.add_heading(TITULO, level=0)
        titulo.alignment = ALINHAMENTO_CENTRAL

    def add_valor(self):
        valor = self.document.add_paragraph()
        run_valor = valor.add_run(f"R${self._valor:.2f}")
        run_valor.font.size = VALOR_FONT_SIZE
        valor.alignment = ALINHAMENTO_DIREITA
        valor.paragraph_format.space_before = ESPACAMENTO_24
        valor.paragraph_format.space_after = ESPACAMENTO_72

    def add_corpo(self):
        corpo = self.document.add_paragraph('Recebi de "')
        corpo.alignment = ALINHAMENTO_JUSTIFICADO
        run_corpo = corpo.add_run({self._pagador._nome.upper()})
        run_corpo.bold = True
        corpo.add_run(
            f'", inscrito no {self._pagador.tipo_pessoa()} n° {formatar_doc(self._pagador._documento)}, a importância de R${self._valor:.2f} ({formatar_numero_extenso(self._valor)}), referente ao {self._referencia}.'
        )

    def add_data_assinatura(self):
        data = self.document.add_paragraph()
        data.alignment = ALINHAMENTO_CENTRAL
        data_run = data.add_run(
            f"{self._cidade} - {self._estado.upper()}, {formatar_data(self._data)}."
        )
        data.paragraph_format.space_after = ESPACAMENTO_72
        data.paragraph_format.space_before = ESPACAMENTO_50

        assinatura = self.document.add_paragraph()
        assinatura.add_run("\n\n")
        assinatura.add_run(
            "__________________________________________________________________________"
        )
        assinatura.alignment = ALINHAMENTO_CENTRAL

    def add_recebedor(self):
        nome_recebedor = self.document.add_paragraph()
        nome_recebedor.alignment = ALINHAMENTO_CENTRAL
        nome_recebedor_run = nome_recebedor.add_run(f"{self._recebedor.nome_upper()}")
        documento_recebedor = self.document.add_paragraph()
        documento_recebedor_run = documento_recebedor.add_run(
            f"{self._recebedor.tipo_pessoa()}: {formatar_doc(self._recebedor._documento)}"
        )
        documento_recebedor.alignment = ALINHAMENTO_CENTRAL

    def salvar_recibo(self):
        self.document.save(f"{self._nome}.docx")

    def criar_recibo(self):
        self.add_titulo()
        self.add_valor()
        self.add_corpo()
        self.add_data_assinatura()
        self.add_recebedor()