def combine_dicts(d1,d2):
    """
    :result - результат объединения двух словарей без изменений
    d1 - первый словарь
    d2 - второй словарь
    """
    result = {**d1,**d2}
    return result