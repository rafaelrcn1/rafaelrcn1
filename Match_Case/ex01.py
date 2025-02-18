
nome_produto = str(input("Digite o nome do produto\n "))
preco = float(input("Digite o preço do produto\n "))

match nome_produto:
    case "Smartphone":
        print(f"O preço com desconto é: {preco*0.9:.1f}")
    case "Tablet":
        print("O preço com desconto é: ", preco*0.85)
    case "Laptop":
        print("O preço com desconto é:", preco*0.8)
    case _: #produto inexistente
        print("O produto escolhido não tem desconto e seu preço final é:", preco)