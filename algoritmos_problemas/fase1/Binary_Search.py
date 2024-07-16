

# Retorna a posição de x no array arr
def buscaBinaria(arr, baixo, alto, x):

    while baixo <= alto:

        meio = baixo + (alto - baixo) // 2

        # Verifica se x está presente no meio
        if arr[meio] == x:
            return meio

        # Se x é maior, ignora a metade esquerda
        elif arr[meio] < x:
            baixo = meio + 1

        # Se x é menor, ignora a metade direita
        else:
            alto = meio - 1

    # Se chegarmos aqui, o elemento não está presente
    return -1


# Código Principal
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]  # Define o array de elementos
    x = 10                   # Define o elemento a ser buscado

    # Chama a função de busca binária
    resultado = buscaBinaria(arr, 0, len(arr)-1, x)
    
    # Verifica se o elemento foi encontrado
    if resultado != -1:
        print("O elemento está presente no índice", resultado)  # Se encontrado, imprime o índice do elemento
    else:
        print("O elemento não está presente no array")          # Se não encontrado, imprime que o elemento não está no array
