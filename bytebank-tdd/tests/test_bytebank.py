from codigo.bytebank import Funcionario

# 1 primeiro test:
class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_24(self):
        entrada = '13/03/2000' # Given- contexto
        esperado = 24

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade # When-ação

        assert resultado == esperado # Then-desfecho

    # 2 segundo test:

    def test_quando_sobre_recebe_Lucas_carvalho_deve_retorna_Carvalho(self):
        entrada = 'Lucas Carvalho' # Given-contexto
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() # When

        assert resultado == esperado

    # 3 terceiro teste
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 # Given
        entrada_nome = 'Paulo Braganca'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # When
        resultado = funcionario_teste.salario

        assert resultado == esperado # Then
