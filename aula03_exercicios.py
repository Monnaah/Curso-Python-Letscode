idade = int(input('Digite sua idade:'))
if idade >= 18:
    print ('maior de idade')
else:
    print ('menor de idade')


"""Faça um programa que leia a validade das informações:

a. Idade: entre 0 e 150;

b. Salário: maior que 0;

c. Sexo: M, F ou Outro;

O programa deve imprimir uma mensagem de erro para cada informação inválida.
"""

idade = int(input('Digite a idade: '))

while idade < 0 or idade > 150:
    print('Erro! Idade deve estar entre 0 e 150!')
    idade = int(input('Digite a idade: '))

salario = float(input('Digite seu salario: '))
while salario < 0:
    print('Erro. O salario deve ser maior que 0')
    salario = float(input('Digite seu salario: '))

genero = input('Digite seu genero(M/F/O): ')
while genero !='m' and genero !='f' and genero !='o': 
    print(type(genero))
    print('Erro!Digite seu genero(M/F/O) ')
    genero = input('Digite seu genero(M/F/O): ')

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2)/2

if media >= 6.0:
    print('Aprovado')
if media < 6.0:
    print('Reprovado')

print('Média: ', media)
