def main():
    from models.pessoa import Pessoa
    from models.recibo import Recibo

    nome_recibo = "Recibo arrendamento de pasto - Adriano"  # input('Digite o nome do recibo criado: ')#
    valor_recibo = 350  # input float
    referencia_recibo = "pagamento do arrendamento do pasto para colocar gado no Jardim dos Lagos, na cidade Águas de Lindóia - SP. (04 cabeças), referente ao mês de Fevereiro de 2024"  # input str
    data_recibo = "19/04/2024"  # input str
    cidade_recibo = "Monte Sião"  # input str
    estado_recibo = "MG"

    pagador = Pessoa("Gustavo Rodrigues Lopes", "09825330635")
    recebedor = Pessoa("Portucale Imóveis", "05302130000100")
    recibo = Recibo(pagador, recebedor, nome_recibo, valor_recibo, referencia_recibo, data_recibo, cidade_recibo, estado_recibo)
    recibo.criar_recibo()


if __name__ == "__main__":
    main()