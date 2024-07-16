



def bubbleSort(arr):
    n = len(arr)
    
    # Percorre todos os elementos do array
    for i in range(n):
        trocado = False

        # Os últimos i elementos já estão no lugar
        for j in range(0, n-i-1):

            # Percorre o array do índice 0 até n-i-1
            # Troca se o elemento encontrado for maior
            # que o próximo elemento
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocado = True
        # Se não houve troca, o array já está ordenado
        if not trocado:
            break


# Código principal para testar a função acima
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)

    print("Array ordenado:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")


