import math

def jumpSearch(arr, x, n):
    # Encontrar o tamanho do bloco a ser saltado
    step = math.sqrt(n)

    # Encontrar o bloco onde o elemento está
    # presente (se estiver presente)
    prev = 0
    while arr[int(min(step, n) - 1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    # Fazer uma busca linear para x no
    # bloco começando com prev.
    while arr[int(prev)] < x:
        prev += 1

        # Se chegarmos ao próximo bloco ou ao fim
        # do array, o elemento não está presente.
        if prev == min(step, n):
            return -1

    # Se o elemento for encontrado
    if arr[int(prev)] == x:
        return prev

    return -1

# Código de teste para a função
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
       34, 55, 89, 144, 233, 377, 610]
x = 55
n = len(arr)

# Encontrar o índice de 'x' usando Jump Search
index = jumpSearch(arr, x, n)

# Imprimir o índice onde 'x' está localizado
print("Número", x, "está no índice", "%.0f" % index)
