salario = float(input("Qual é o valor de seu salário mensal?: "))
imposto1 = 15
imposto2 = 20
bonus_fixo = 500

if salario <= 2000:
    print("Parabéns, você não pagará impostos :)")
if salario > 2000 and salario  <=4000:
    valor_imposto = salario * (imposto1 / 100)
    salario_liquido = salario - valor_imposto
    print(f"Imposto a pagar: R${valor_imposto:.2f}")
    print(f"Salário líquido: R${salario_liquido:.2f}")

if salario > 4000:
    valor_imposto = salario * (imposto2 / 100)
    salario_liquido = salario - valor_imposto + bonus_fixo
    print(f"Imposto a pagar: R${valor_imposto - 500:.2f}")
    print(f"Salário líquido: R${salario_liquido:.2f}")