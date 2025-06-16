notas = [10, 9, 8.5, 9.5]
soma = 0
x = 0

while x < 4:
	soma = soma + notas [x]
	x = x + 1
	média = soma / x

if média >= 6:
    print (f"A média do aluno é: {média}. Está aprovado")
else:
    print (f"A média do aluno é: {média}. Está reprovado")