from bisect import bisect_left

# Função para realizar a busca Fibonacci
def fibMonaccianSearch(arr, x, n):

    # Inicializa os números de Fibonacci
    fibMMm2 = 0  # (m-2)-ésimo número de Fibonacci
    fibMMm1 = 1  # (m-1)-ésimo número de Fibonacci
    fibM = fibMMm2 + fibMMm1  # m-ésimo número de Fibonacci

    # Calcula o menor número de Fibonacci que é maior ou igual ao tamanho do array
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    # Marca o intervalo eliminado a partir do início
    offset = -1

    # Enquanto houver elementos para inspecionar
    # Nota: comparamos arr[fibMMm2] com x.
    # Quando fibM se torna 1, fibMMm2 se torna 0
    while (fibM > 1):

        # Verifica se fibMMm2 é uma posição válida no array
        i = min(offset + fibMMm2, n - 1)

        # Se x é maior que o valor no índice fibMMm2,
        # corta o subarray do offset até o índice i
        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i

        # Se x é menor que o valor no índice fibMMm2,
        # corta o subarray após o índice i + 1
        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1

        # Elemento encontrado. Retorna o índice
        else:
            return i

    # Comparando o último elemento com x
    if (fibMMm1 and arr[n - 1] == x):
        return n - 1

    # Elemento não encontrado. Retorna -1
    return -1

# Código de teste
arr = [10, 22, 35, 40, 45, 50,
       80, 82, 85, 90, 100, 235]
n = len(arr)
x = 235
ind = fibMonaccianSearch(arr, x, n)
if ind >= 0:
    print("Encontrado no índice:", ind)
else:
    print(x, "não está presente no array")
