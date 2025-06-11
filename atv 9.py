cigarros_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: ")) 
anos_fumando = int(input("digite a quantidade de anos fumando: "))
cigarros_por_ano = cigarros_por_dia * 365 * anos_fumando
tempo_perdido = cigarros_por_ano * 10 / 60 / 24
print("Você perdeu %.2f dias de vida fumando." % tempo_perdido)