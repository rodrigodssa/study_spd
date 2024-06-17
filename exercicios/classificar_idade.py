

def classificar_idade(idade):
    if idade < 0:
        return 'Idade invalida'
    elif idade <= 12:
        return 'Crianca'
    elif idade <= 19:
        return 'Adolecente'
    elif idade <= 64:
        return 'Adulto'
    else:
        return 'Idoso'
    
idade = int(input('Digite a idade: '))
print(classificar_idade(idade))    