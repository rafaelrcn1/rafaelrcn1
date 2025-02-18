#Escreve um programa que calcule a soma e o produto dos N primeiros números naturais.

y = 0
z = 1
x = int(input("Introduza um número para calcular a soma: "))

for i in range(1,x+1):
    y += i
    z *= i
    
print(y)

    