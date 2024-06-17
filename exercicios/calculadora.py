

def calculadora(num1, num2, operacao):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Divisão por zero não é permitida'
    else:
        return 'Operacao invalida'

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
operacao = input('Digite a operacao(soma, subtracao, multiplicacao, divisao): ').lower()
print(calculadora(num1, num2, operacao))    
