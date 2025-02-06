#Implemente uma calculadora simples com as operações aritméticas básicas. O utilizador deverá especificar a 
# operação desejada (+,-,*,/) e, em seguida, inserir dois valores. Caso, o utilizador escolha divisão e insira como 
# valor do denominar 0 mostra uma mensagem personalizada. 
# Para os restantes casos, mostra no ecrã o resultado da operação desejada.

operacao = str(input("Digite a operação desejada, escolha entre os símbolos '+, -, * ou /'\n "))

numero_1 = float(input("Escolha o primeiro número"))
numero_2 = float(input("Escolha o segundo número"))

if operacao == "+":
    print(numero_1 + numero_2)
elif operacao == "-":
    print(numero_1 - numero_2)
elif operacao == "*":
    print(numero_1 * numero_2)
elif operacao == "/" and numero_2 == 0:
    print("Não pode inserir o valor 0")
elif operacao == "/":
    print(numero_1 / numero_2)
else:
    print("Operação inválida")
    