
def validar_senha(senha):
    if len(senha) < 8:
        return 'Senha invalida: deve ter no minimo 8 caracteres.'
    
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_simbolo = False
    simbolos_especiais = '!@#$%^&*(),.?\":{}|<>'

    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_numero = True
        elif char in simbolos_especiais:
            tem_simbolo = True            

    if not tem_maiuscula:
        return 'Senha invalida: deve conter pelo menos uma letra maiuscula.'
    if not tem_minuscula:
        return 'Senha invalida: deve conter pelo menos uma letra minuscula.'
    if not tem_numero:
        return 'Senha invalida: deve conter pelo menos um numero.'
    if not tem_simbolo:
        return 'Senha ivalida: deve conter pelo menos um simbolo especial.'

    return 'Senha invalida'

senha = input('Digite uma senha:')
print(validar_senha(senha))
