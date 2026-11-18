def is_palindrome(value):
    """
    :value[::-1] - читатет value задом-наперед
    :value - параметр для функции
    """
    str_value = str(value)
    if str_value.lower() == str_value[::-1].lower():
        return True
    else:
        return False
    