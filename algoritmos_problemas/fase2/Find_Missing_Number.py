def missing_number(n, arr):
    # Cria um array de hash de tamanho n+1
    hash = [0] * (n + 1)

    # Armazena as frequências dos elementos
    for num in arr:
        hash[num] += 1

    # Encontra o número ausente
    for i in range(1, n + 1):
        if hash[i] == 0:
            return i

    # Tratamento de caso especial (embora o problema garanta uma solução)
    return -1


# Código de teste
arr = [1, 2, 3, 5]
n = 5
print(missing_number(n, arr))
