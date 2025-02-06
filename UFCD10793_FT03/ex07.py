
ano = int(input("Digite seu ano\n "))
   
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print("Ano Bissexto")
else: 
    print("Ano não é bissexto")
