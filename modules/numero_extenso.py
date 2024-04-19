from num2words import num2words

def number_to_long_number(value):
    # Primeiro, separamos o número em reais e centavos
    real_part = int(value)
    centavo_part = int(round((value - real_part) * 100))
    
    # Convertendo a parte dos reais
    if real_part == 1:
        real_text = num2words(real_part, lang='pt_BR') + " real"
    else:
        real_text = num2words(real_part, lang='pt_BR') + " reais"
    
    # Convertendo a parte dos centavos
    if centavo_part == 1:
        centavo_text = num2words(centavo_part, lang='pt_BR') + " centavo"
    else:
        centavo_text = num2words(centavo_part, lang='pt_BR') + " centavos"
    
    # Combinando as duas partes
    if real_part > 0 and centavo_part > 0:
        return f"{real_text} e {centavo_text}"
    elif real_part > 0:
        return real_text
    elif centavo_part > 0:
        return centavo_text
    else:
        return "zero reais"


