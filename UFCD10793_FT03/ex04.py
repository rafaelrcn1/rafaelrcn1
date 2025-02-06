#Escreve um programa que receba dois números reais e indique qual o maior dos dois números. 
# Considera a possibilidade de o utilizador indicar dois números iguais.

num_real = float(input("Digite seu primeiro número:\n "))
segundonum = float(input("Digite seu segundo número:\n "))
                  
if num_real > segundonum:
    print(num_real, "é maior que ,", segundonum)
elif num_real == segundonum:
    print("Números iguais")
else:
    print(num_real, "é menor que ", segundonum)
    
