import doctest

def adult(age):
    return 'adult' if age >= 18 else 'not adult'

doctest.testmod()