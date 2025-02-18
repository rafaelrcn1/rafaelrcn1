#Escreva um programa que solicite ao utilizador dois números inteiros a
#operação matemática a ser realizada (+,-,* e /). 

num1 = float(input("Digite o primeiro número\n "))
num2 = float(input("Digite o segundo número\n "))

operacao = str(input("Digite qual operação você quer realizar? Escolha entre +, -, * ou /\n "))

match operacao:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
        
    case "/": 
        if num2 == 0:
            print("Não podemos dividir por 0")
        else:
            print(num1/num2)
            
            
    case _:
        print("Operação inválida")