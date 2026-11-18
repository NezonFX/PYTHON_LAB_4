def are_anagrams(a,b):
    """
    :a.sort() - сортируем первую строку
    :b.sort() - сортируем вторую строку 
    """
    if sorted(a.lower()) == sorted(b.lower()):
        return True
    else:
        return False