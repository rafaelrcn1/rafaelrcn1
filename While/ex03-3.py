#Fazer um programa para ler quatro números inteiros e positivos, calcular e devolver a sua média.

contador = 1
soma = 0

while contador <=4:
     numero = int(input(f"Introduza o {contador}º número: "))
     soma = soma + numero
     contador = contador+1
     

media = soma / (contador-1)

print(f"A média dos números introduzidos é {media}")