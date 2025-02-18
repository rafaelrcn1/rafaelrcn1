nums = [10, 2.5, 7, 11, 7.9, "Python", True, 6, 5.8, "Listas"]

# Inicializa contadores para cada tipo de dado
int_count = 0
float_count = 0
str_count = 0
bool_count = 0

# Itera sobre a lista e verifica o tipo de cada elemento
for item in nums:
    if type(item) == int:
        int_count += 1
    elif type(item) == float:
        float_count += 1
    elif type(item) == str:
        str_count += 1
    elif type(item) == bool:
        bool_count += 1

# Imprime a quantidade de cada tipo de dado
print("Quantidade de inteiros:", int_count)
print("Quantidade de floats:", float_count)
print("Quantidade de strings:", str_count)
print("Quantidade de booleanos:", bool_count)

#Exercício B

soma_inteiros = 0
contador_inteiros = 0

for elemento in nums:
    try:
        # Tenta converter o elemento para um inteiro
        valor_inteiro = int(elemento)
        soma_inteiros += valor_inteiro
        contador_inteiros += 1
    except ValueError:
        # Se a conversão falhar, o elemento não é um inteiro
        pass

if contador_inteiros > 0:
    media_inteiros = soma_inteiros / contador_inteiros
    print("A média dos valores inteiros na lista é:", media_inteiros)
else:
    print("Não foram encontrados valores inteiros na lista.")
    
    