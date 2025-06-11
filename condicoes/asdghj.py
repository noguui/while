categoria = int(input("Digite a categoria do produto (1 a 5): "))

if categoria == 1:
    print("O preço do produto é R$10")
else:
    if categoria == 2:
        print("O preço do produto é R$20")
    else:
        if categoria == 3:
            print("O preço do produto é R$30")
        else:
            if categoria == 4:
                print("O preço do produto é R$40")
            else:
                if categoria == 5:
                    print("O preço do produto é R$50")
                else:
                    print("Categoria inválida!")