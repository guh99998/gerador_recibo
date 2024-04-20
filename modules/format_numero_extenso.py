from num2words import num2words

def formatar_numero_extenso(valor):
    '''
    Formata um valor no formato '350' para 'trezentos e cinquenta reais'

    :param valor: Int ou Float representando o valor.
    :return: String formatada com o valor por extenso.
    '''
    parte_real = int(valor)
    parte_centavos = int(round((valor - parte_real) * 100))

    if parte_real == 1:
        texto_real = num2words(parte_real, lang='pt_BR') + " real"
    else:
        texto_real = num2words(parte_real, lang='pt_BR') + " reais"

    if parte_centavos == 1:
        texto_centavos = num2words(parte_centavos, lang='pt_BR') + " centavo"
    else:
        texto_centavos = num2words(parte_centavos, lang='pt_BR') + " centavos"

    if parte_real > 0 and parte_centavos > 0:
        return f"{texto_real} e {texto_centavos}"
    elif parte_real > 0:
        return texto_real
    elif parte_centavos > 0:
        return texto_centavos
    else:
        return "zero reais"


