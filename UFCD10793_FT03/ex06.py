#Escreve um programa que receba três números reais e indique qual o maior dos três números.

numero1 = float(input("Digite seu número"))
numero2 = float(input("Digite seu número"))
numero3 = float(input("Digite seu número"))

if numero1 >= numero2 and numero1 >= numero3:
    print(numero1) 
elif numero2 >= numero1 and numero2 >= numero3:
    print(numero2) 
else:
   print(numero3)