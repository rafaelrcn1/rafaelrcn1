#Escreva um programa que verifique se um determinado número 
# introduzido pelo utilizador é nulo, positivo ou negativo.

numero = float(input("Digite seu número"))

if numero == 0:
    print("Seu número é nulo")
elif numero < 0:
    print("Seu número é negativo")
else:
    print("Seu número é positivo") 