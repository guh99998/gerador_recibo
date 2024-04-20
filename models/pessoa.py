class Pessoa:
    def __init__(self, nome, documento):
        self._nome = nome
        self._documento = documento

    def nome_upper(self):
        ''''
        Formata uma string recebida, deixando a string inteira com letras maiúsculas
        '''
        return self._nome.upper()

    def tipo_pessoa(self):
        if len(self._documento) == 11:
            return 'CPF'
        else:
            return 'CNPJ'