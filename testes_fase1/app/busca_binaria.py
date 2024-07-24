# busca_binaria.py

def buscaBinaria(arr, baixo, alto, x):
    while baixo <= alto:
        meio = baixo + (alto - baixo) // 2
        if arr[meio] == x:
            return meio
        elif arr[meio] < x:
            baixo = meio + 1
        else:
            alto = meio - 1
    return -1

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    resultado = buscaBinaria(arr, 0, len(arr)-1, x)
    if resultado != -1:
        print("O elemento está presente no índice", resultado)
    else:
        print("O elemento não está presente no array")
