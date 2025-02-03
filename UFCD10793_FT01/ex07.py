#Faz um programa que receba a distância em km e a quantidade em litros de
#combustível consumido por um carro num percurso. Calcula o consumo km/l e escreve
#uma mensagem de acordo com o resultado obtido.

km = float(input("Quantos km percorreu?\n-> "))
litros = float(input("Quantos litros gastou?\n-> "))

total_gasto = float(round(km/litros,2))

print("O total de combustível gasto foi:" ,total_gasto)