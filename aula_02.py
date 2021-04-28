# Observações sobre nome de variáveis
    # No geral, a convenção em python é sempre ter todos os caracteres minusculos
    #  e palavras separadas por underline (_) 

    # Coisas que são legais de evitar: 
        # 1. Palavras reservadas pelo Python - as que ficam coloridas
        #   if else lambda def assert with elif tuple for while input   
        # 2. Acento 
        # 3. Abreviações extremas (idade_em_anos -> iea (ruim)), a, b, c 
        # 4. Nomes extremamente longos
        # 5. Misturar linguas -> se quiser codar em português, todas as variáveis
            # precisam ficar em português

    # Coisas que não podemos fazer nos nomes de variáveis
        # 1. Espaço no nome -> idade em anos (errado) -> vai gerar um erro
        # 2. Começar por número -> 18_anos_ou_mais (errado) -> vai gerar um erro

    # Conclusão: sempre que escrever uma variável, seguir o padrão
        # Exemplos de nomes de variáveis: nome, numero_leads, num_leads, num_quartos,
        # maior_que_18


# Tipos de variáveis/ tipos de dados
# 4 tipos principais



# 1. Tipo inteiro (int): para números inteiros (sem casa decimal)
# Exemplos:  1, 400, -400, 0 

# Se eu quisesse registrar a idade de uma pessoa em anos em uma variável,
idade_em_anos = 15 # Variável "idade_em_anos" recebe o valor 15 no formato int



# 2. Tipo float (float): para números com casas decimais. Tem aplicações mais abrangentes
#   que o tipo int -> geralmente, vai ser o tipo de dado padrão para receber informações
#   externas. 
# Exemplos: 10.5, -21.0 (número int representado como float), 0.0


valor_produto = 4.99 # Preço de uma coca cola em reais/ centavos  
altura = 1.78 # Em metros/ cm




# 3. Tipo string (str): representam textos, que devem ser indicados com aspas simples ''
#   ou aspas duplas "". Strings podem conter acentos, espaço, caracteres especiais, etc
    # Observação importante (avançada):
    # Se quisermos representar aspas dentro de um texto, precisamos 
    # alternar os simbolos -> não pode fazer '''' ou """".

# Exemplos: "Hello, world!"

ola_mundo = "Hello, world!"
nome_completo = 'Simone Simões'

# Observação simples: é legal adotar uma das aspas e manter ela ao longo de todo seu código
# Se você usou aspas simples na primeira linha, é legal manter todos os outros strings
# representados por aspas simples.




# 4. Tipo booleano (bool): Verdadeiro (True / 1) ou Falso (False / 0)

# Exemplos: comparações
maior_que_18 = True 



# Variáveis são mutáveis - python deixa mudar o valor e o tipo de dado de uma variável
# quando quisermos :)

# Vamos mudar o valor e preservar o tipo
idade = 15
idade = 17

# Vamos preservar o valor e mudar o tipo
idade = 17
idade = 17.0

# Vamos mudar os dois ao mesmo tempo
idade = 17.0
idade = 'boa noite'

## Comentários -> linhas começadas pelo hashtag "#"
# São utilizados para explicar melhor um trecho de código 
# Aqui, não preciso seguir a sintaxe de Python, então posso colocar espaços, caracteres
# especiais, etc
# Eu diria que são tão importantes quanto o código em si
#   Observações:
#      - É legal fazer na mesma lingua que você utilizou para
#           o nome das variáveis
#      - É legal ter um balanço entre quantidade de código e de comentário


# Isso é um comentário de uma linha só

'''
Aqui, eu posso escrever um comentário
que ocupa múltiplas linhas. Para tal, só preceder o comentário
de múltiplas linhas com três aspas simples ou três aspas duplas, 
colocando também no final. Esse "comentário" é interpretado
pelo Python como uma string.
'''

# Saída (output)
# É a forma que o computador apresenta dados de saída para um usuário.
# Em Python, na maioria das vezes, isso é feito com a função print

# Jargão muito utilizado: "printar" alguma coisa

# Exemplo - vamos "printar" coisas
print('Olá, mundo!')
print(10)
print(-27.36)
print(3.141592654)
# print(False) # Para "ocultar", só comentar a linha


# Podemos "printar" variáveis
nome = 'Lucas Miura'
print(nome) # Quando printamos uma variável, o "conteúdo" dela é mostrado na tela


# Outra coisa - podemos passar várias coisas para printar de uma só vez
print('nome: Lucas Miura', 'idade: 21', 'ocupação: professor')

# Só separar com vírgula 
print('nome: Lucas Miura | idade:', 21, '| maior que 18 anos:', True)
print('idade:', 21)
print('Maior que 18 anos:', True)


# Entrada (input)
# É a forma como o computador coleta dados de entrada do usuário
# Existem outras formas (ler um arquivo/ tabela, por ex),
# mas nesse comecinho, vamos fazer a entrada com um novo comando:

# Sempre que colocar um input, na hora de rodar o código,
# O python vai pausar a execução nessa linha e esperar um input do usuário

#idade = input('Por favor, preencha sua idade: ')
#print(idade)

# Sempre que fazemos um input, o dado é interpretado como string!
# Podemos usar o comando type para ver o tipo de dado
# nome = 'Lucas'
# type(nome) -> <class 'str'>
#print(type(idade))

# Como já receber o dado na forma numérica?
idade = int(input('Por favor, preencha sua idade: '))
print(idade)
print(type(idade))

# Quando o dado pode ter casas decimais, transformamos para float
altura = float(input('Por favor, preencha sua altura \n\
(altura em metros, casas decimais separadas por ponto. Ex: 1.78): '))
print(altura)
print(type(altura))

# Nosso programa deve funcionar para o usuário ideal 

# Para transformar um número em texto,
numero = 10
numero_em_formato_str = str(numero)
print(numero_em_formato_str)



# Operações numéricas em Python
print(1+1.0) # -> 2.0
print(2 - 5) # -> -3 
print(2*2) # -> 4
print(3/2) # -> 1.5
print(3 // 2) # -> 1
print(3 % 2 ) # -> 1 (resto da divisão
print(2**3) # 2*2*2 -> 8

idade = 15
idade_2 = 18.0

idade_3 = idade - idade_2
