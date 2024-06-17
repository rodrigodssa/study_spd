

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc < 24.9:
        return 'Peso normal'
    elif imc < 29.9:
        return 'Sobrepeso'
    else:
        return 'Obeso'


peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
print(calcular_imc(peso, altura))
            