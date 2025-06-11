total = 0
for i in range(5):
    valor = float(input('Digite o valor do produto: '))
    total = total + valor

desconto = total * 0.15
total_com_desconto = total - desconto

print(f'O valor final de suas compras é de R$ {total_com_desconto:.2f} . Você ainda economizou R$ {desconto:.2f} devido ao desconto de 15% que foi dado especialmente para você.') 