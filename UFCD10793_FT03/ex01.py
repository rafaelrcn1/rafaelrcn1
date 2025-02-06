#Escreve um programa que solicite um número inteiro ao utilizador e caso o mesmo seja maior que 20, devolva o resultado da sua divisão por 2.

numero = int(input("Escolha um número\n -->"))

if numero > 20:
    print(numero/2)
else:
    print("Número menor ou igual a 20!")
