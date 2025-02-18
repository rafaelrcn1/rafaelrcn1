idades =[25, 15, 19, 22, 37, 78, 46, 2, 67]
print(idades)

#Ordene a lista por ordem decrescente

contador = 0

for numero in idades:
  if numero < 18:
    contador += 1
print(contador)



idades.sort(reverse=True)
print(idades)



#c. Pede ao utilizador uma idade e verifica se essa idade está na lista.
#- Se estiver faz print("A idade está na lista")
#- Caso contrário faz o print("não existe ninguém com essa idade na lista")

x = int(input("Digite sua idade: "))

if x in  idades:
        print("A idade está na lista")
else:
        print("A idade não está na lista")
        
        
menores_idade = [x for x in idades if x<18]