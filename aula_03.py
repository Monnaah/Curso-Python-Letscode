############################### Revisão ############################### 
'''# Variáveis
var = 10 # var recebe o valor 10

# Input (input) e output (print)
idade = input('Digite sua idade: ') # input coleta informações do usuário

print('Sua idade é:', idade) # Imprime na tela do PC

# Tipos de dados - tipos, conversão e operações
# 4 tipos - int, float, str, bool
# int - numérico sem casa decimal
print('Exemplos de int:', 1, 2, -5, 0)

# float - numérico com casa decimal
print('Exemplos de float:', 1.5, 0.0, -2.5, 15000.12345)

# str - basicamente texto 
print('Exemplos de str:', 'Olá, mundo!', 'Meu nome é Lucas')

# bool - booleano / binário - valores lógicos
print('Exemplos de bool:', True, False)

# Operações matemáticas - números
print('Soma:',5 + 5)
print('Subtração', 5 - 5)
print('Multiplicação', 5*2)
print('Divisões')
print('Divisão com casa decimal', 5/2) 
print('Divisão sem casa decimal', 5//2)
print('Resto da divisão', 5%2)
print('Potenciação', 5**2)

# Priorizar contas com parênteses
# Ordem padrão das operações -> ** -> *, / -> +, -
print( (5+5)/2              ) # -> 5
print(  5 + 5/2             ) # -> 7.5'''


########################################################################
# Aula 3 
# Observação - nunca se deixe intimidar por nomes em tecnologia
# Operadores lógicos 

# São utilizados para comparar valores e/ou variáveis
# Sempre retornará True ou False

# Maior que: >
print('3 > 1', 3 > 1) # True

# Maior ou igual: >=
print('2 >= 2',2 >= 2) # True

# Menor que: <
print('3 < 1', 3 < 1) # False 

# Menor ou igual que: <=
print('2 <= 2',2 <= 2) # True

# Igual: ==
print('2 == 2',2 == 2) # True

# Diferente: !=
print('3 != 1',3 != 1) # True

numero = 100
print('numero = 100')
print('numero < 10', numero < 10) # False
print('numero == 100', numero == 100) # True
print('numero == 100.0', numero == 100.0) # True (eu evitaria)

numero = 100.0
print('numero == 100', numero == 100)

# Como funciona comparação de texto?
texto = 'Simone Simoes'
print(texto == 'Simone A Simões') # False
print(texto == 'simone simoes') # False -> Python diferencia maiúsculo de minúsculo em str

print("'100' > '101'", '100' > '101') # Ordem alfabética
print("'a' > 'b'", 'a' > 'b' )
print("'a' < 'b'", 'a' < 'b' )
print("'A' < 'zz'", 'A' < 'zz')

print("'A' > 'a'", 'A' > 'a')

print('a, b, c, d, e') 
print("'!' == 1",'!' == 1)

# Existem muitas comparações que podemos fazer - a questão é que a maior parte delas
# não é convencional

# and e or
# and - só é True se ambas as comparações forem True
# Por exemplo,
print( (1 == 1) and (2 > 1) ) # True and True -> True
print(True and False) # False
print(False and False) # False
print(True and True) # True

idade = 18
sexo = 'F'

# Vamos verificar se a pessoa de idade 18 e sexo 'F' pertence ao público alvo
# Feminino de idade entre 18 e 25 anos.

filtro_idade = idade >= 18 and idade <= 25 # True
filtro_sexo = sexo == 'F' # True

pertence_ao_publico_alvo = filtro_idade and filtro_sexo
print('pertence_ao_publico_alvo', pertence_ao_publico_alvo)

# or: é True se pelo menos uma das comparações for True
print(True or False) # True
print(True or True) # True
print(False or True) # True
print(False or False) # False


# Parênteses - analogia com números
# or -> +
# and -> *
# (0 + 1) + 1*0 -> 1 
# (False or True) or True and False


####################################################
# Estruturas Condicionais
# if | elif | else

idade = 15

if idade > 30:
    print('Anúncio de Vinho') # Essa linha pertence ao bloco if
    # Esse trecho identado com um tab só será executado
    # se a idade for maior que 18
    # Um bom jeito de separar conteúdo para um público alvo específico
elif idade > 18:
    print('Anúncio de Vodka')
elif idade > 11:
    print('Anúncio de filme de ação (com censura de 11 anos)')
    # Se a idade não for maior do que 18, mas for maior que 11,
    # esse bloco será executado no lugar
else: 
    # Caso nenhuma das condições anteriores forem correspondidas,
    # Caímos no bloco do else
    print('Anúncio de Coca-cola')
