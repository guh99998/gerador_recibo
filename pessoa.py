class Pessoa:
    def __init__(self, nome, documento):
        self._nome = nome
        self._documento = documento

    def nome_upper(self):
        return self._nome.upper()