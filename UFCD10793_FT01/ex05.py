#Sejam a e b os catetos de um triângulo retângulo, faz um programa que devolva o valor da hipotenusa

a = float(input("Digite o valor de a\n-> "))
b = float(input("Digite o valor de b\n-> "))

hipotenusa = float((a**2 +b**2)**0.5)

print("O valor da hipotenusa é:", hipotenusa)