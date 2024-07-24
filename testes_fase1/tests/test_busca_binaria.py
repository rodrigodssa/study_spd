# test_busca_binaria.py

from app.busca_binaria import buscaBinaria

def test_busca_binaria():
    arr = [2, 3, 4, 10, 40]
    assert buscaBinaria(arr, 0, len(arr)-1, 10) == 3
    assert buscaBinaria(arr, 0, len(arr)-1, 3) == 1
    assert buscaBinaria(arr, 0, len(arr)-1, 40) == 4
    assert buscaBinaria(arr, 0, len(arr)-1, 1) == -1
    assert buscaBinaria([], 0, -1, 10) == -1
