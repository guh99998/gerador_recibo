def formatar_doc(documento):
    if len(documento) == 11:
        documento = documento.zfill(11)
        cpf = '{}.{}.{}-{}'.format(documento[:3], documento[3:6], documento[6:9], documento[9:])
        return cpf
    elif len(documento) == 14:
        documento = documento.zfill(14)
        cnpj = '{}.{}.{}/{}-{}'.format(documento[:2], documento[2:5], documento[5:8], documento[8:12], documento[12:])
        return cnpj
    else:
        print(f'O documento {documento} não é um documento válido')