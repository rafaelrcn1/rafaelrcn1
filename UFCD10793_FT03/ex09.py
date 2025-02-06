#O Índice de Massa Corporal (IMC) é utilizado para medir o peso ideal de uma pessoa. 
# Escreve um programa que peça o nome, a idade, o peso e a altura do utilizado e que, 
# de seguida, calcule e mostre o resultado do seu IMC e classifique esse resultado de acordo 
# com as seguintes condições:

nome = str(input("Digite seu nome\n "))
idade = int(input("Digite sua idade\n "))
peso = float(input("Digite seu peso\n "))
altura = float(input("Digite sua altura\n "))

imc = peso/altura**2

if imc < 17:
    print("Muito abaixo")
elif imc >= 17  and imc < 18.5:
    print("Abaixo do peso")
elif imc >=18.5 and imc< 25:
    print("Normal")
elif imc >= 18.5  and imc < 25:
    print("Normal")

    