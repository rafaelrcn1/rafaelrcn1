#b. Utilizando estruturas de repetição escreva um programa que mostre os
#resultados da tabuada de multiplicação dos números entre 1 e 10, como segue.

for valor in range(1,11):
    for numero in range(1,11):
        print(f'{valor} * {numero} = {valor*numero}')
        
        
'''Ou.... Solução 2'''

x=1
while x<=10:
    y=1
    while y<=10:
        print(f'{x} * {y} = {x*y}')
        y+=1
    x+=1
    
