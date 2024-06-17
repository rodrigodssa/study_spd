

def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Impar'
    
numero = int(input('Digite um numero: '))
print(par_ou_impar(numero))    