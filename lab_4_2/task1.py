def count_words(sentence):
    """
    :sentence - str, параметр для функции
    :return - int, возвращает длину строки
    """
    if not sentence:
        return 0
    word = sentence.split()
    return len(word)
