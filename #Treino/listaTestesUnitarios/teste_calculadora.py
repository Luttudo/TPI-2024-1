# test_calculator.py

from calculadora import add

def test_add():
    # Testando a adição de números positivos
    assert add(2, 3) == 5

    # Testando a adição de números negativos
    assert add(-2, 3) == 1

    # Testando a adição de zero
    assert add(0, 5) == 5

    # Testando a adição de números decimais
    assert add(1.5, 2.5) == 4.0
