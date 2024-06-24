
def buscar(arr, N, x):
    for i in range(0, N):  # Itera sobre todos os índices do array de 0 a N-1
        if arr[i] == x:  # Se o elemento no índice i for igual a x
            return i  # Retorna o índice i
    return -1  # Se o loop terminar sem encontrar x, retorna -1

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]  # Define o array de elementos
    x = 10  # Define o elemento a ser buscado
    N = len(arr)  # Calcula o tamanho do array

    # Chama a função de busca
    resultado = buscar(arr, N, x)
    
    # Verifica se o elemento foi encontrado
    if resultado == -1:
        print("Elemento não está presente no array")  # Se resultado for -1, o elemento não está no array
    else:
        print("Elemento está presente no índice", resultado)  # Se resultado for diferente de -1, imprime o índice do elemento
