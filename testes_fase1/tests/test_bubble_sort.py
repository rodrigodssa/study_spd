from app.bubble_sort import bubbleSort

def test_bubble_sort():
    # Teste com um array desordenado
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubbleSort(arr)
    assert arr == [11, 12, 22, 25, 34, 64, 90]

    # Teste com um array já ordenado
    arr = [1, 2, 3, 4, 5]
    bubbleSort(arr)
    assert arr == [1, 2, 3, 4, 5]

    # Teste com um array com elementos iguais
    arr = [5, 5, 5, 5, 5]
    bubbleSort(arr)
    assert arr == [5, 5, 5, 5, 5]

    # Teste com um array vazio
    arr = []
    bubbleSort(arr)
    assert arr == []

    # Teste com um array de um único elemento
    arr = [1]
    bubbleSort(arr)
    assert arr == [1]

if __name__ == "__main__":
    test_bubble_sort()
    print("Todos os testes passaram!")
