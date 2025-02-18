#Elabora um programa para escrever no ecrã os números de 1 a 100 e os respetivos quadrados.

contador = 1
quadrado = 1

while contador <= 100:
    print(f"Número: {contador} e seu quadrado é {quadrado}")
    contador = contador + 1
    quadrado = contador ** 2
    
    
''' pode ser assim

i=1
while i<=100:
    print(f"{i}\t{i**2}")
    i=i+1
    
    '''