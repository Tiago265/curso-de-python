# python -m pytest = para testar
# pip install pytest = para baixar o pytest
# ----------------------------------------------------------

# def test_sim():
#     assert sum([1,2,3]) == 7

# -----------------------------------------------------------

# def is_positive(numero):
#     return numero > 0

# def test_eh_positivo():
#     assert is_positive(5) is True
#     assert is_positive(-5) is False

# -----------------------------------------------------------

def somar(a,b):
    return a + b

def comprimento(lista):
    return len(lista)

def test_somar_e_comprimento():
    assert somar(3,2) == 5
    assert comprimento([1,2,3,4,5]) == 5

