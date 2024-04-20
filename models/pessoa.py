class Pessoa:
    def __init__(self, nome, documento):
        self._nome = nome
        self._documento = documento

    def nome_upper(self):
        ''''
        Formata uma string recebida, deixando a string inteira com letras maiúsculas.
        '''
        return self._nome.upper()

    def tipo_pessoa(self):
        '''
        Verifica se a string recebida tem o tamanho para ser um CPF ou se não é considerada um CNPJ.

        :return: String contendo o formato do documento.
        '''
        if len(self._documento) == 11:
            return 'CPF'
        else:
            return 'CNPJ'