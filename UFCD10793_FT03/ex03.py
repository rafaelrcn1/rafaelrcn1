#Escreve um programa que solicite um número inteiro ao utilizador e verifique s
# e o mesmo é par ou ímpar. A mensagem no ecrã deverá ter o seguinte formato;
#O número [número] é [par/ímpar]"
#Nota: um número é par quando o resto da divisão por 2 é zero.

numero = int(input("Digite um número"))

if numero % 2 == 0:
    print(numero, "é um número par.")
else:
    print(numero, "é um número ímpar.")

