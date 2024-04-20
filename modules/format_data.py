import datetime, locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def formatar_data(data_str):
    '''
    Formata uma data 'DD/MM/YYYY' para 'DD de MM de YYYY', ou seja, deixa uma data por extenso.

    :param data_str: String representando a data.
    :return: String formatada da data.
    '''
    data_obj = datetime.datetime.strptime(data_str, "%d/%m/%Y")
    data_formatada = data_obj.strftime("%d de %B de %Y")
    return data_formatada
