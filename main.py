def main():
    from docx import Document
    from docx.shared import Pt
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from modules.format_documento import formatar_doc
    from modules.format_data import formatar_data
    from modules.format_numero_extenso import formatar_numero_extenso
    from pessoa import Pessoa
    from recibo import Recibo

    nome_recibo = "Recibo arrendamento de pasto - Adriano"  # input('Digite o nome do recibo criado: ')#
    # nome_cliente = "Adriano Aparecido de Lima"  # input str
    valor_recibo = 350  # input float
    # cpf_cliente = "05410912632"  # input e opcional str
    referencia_recibo = "pagamento do arrendamento do pasto para colocar gado no Jardim dos Lagos, na cidade Águas de Lindóia - SP. (04 cabeças), referente ao mês de Fevereiro de 2024"  # input str
    data_recibo = "19/04/2024"  # input str
    cidade_recibo = "Monte Sião"  # input str
    estado_recibo = "MG"
    # recebedor = "Évora Administração de Imóveis ltda"  # input str
    # doc_recebedor = "20024324000177"  # input str

    pagador = Pessoa("Gustavo Rodrigues Lopes", "09825330635")
    recebedor = Pessoa("Cintia Carvalho", "12345678910")
    recibo = Recibo(pagador, recebedor, nome_recibo, valor_recibo, referencia_recibo, data_recibo, cidade_recibo, estado_recibo)
    recibo.criar_recibo()
    recibo.salvar_recibo()


if __name__ == "__main__":
    main()
