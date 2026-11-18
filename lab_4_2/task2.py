def find_unique(items):
    """
    :items - исходный список
    :counts - словарь, для подсчета кол-ва жлементов в списке
    :new_items - новый список(результат)
    """
    counts = {}
    new_items = []
    for item in items:
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] +=1
    for key,value in counts.items():
        if value == 1:
            new_items.append(key)
    return new_items