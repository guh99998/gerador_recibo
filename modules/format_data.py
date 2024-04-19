import datetime, locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def formatar_data(data_str):
    data_obj = datetime.datetime.strptime(data_str, "%d/%m/%Y")
    data_formatada = data_obj.strftime("%d de %B de %Y")
    return data_formatada
