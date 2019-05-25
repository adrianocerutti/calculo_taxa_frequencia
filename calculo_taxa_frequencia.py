numero_empregados = float(input("Digite o número de empregados: "))
jornada_mensal_trabalho = float(input("Digite a jornada mensal de trabalho: "))
numero_acidentes = float(input("Digite o número de acidentes: "))
dias_perdidos = float(input("Digite o número de dias perdidos: "))
horas_homens_trabalhadas = numero_empregados * jornada_mensal_trabalho
taxa_frequencia = (numero_acidentes * 1000000) / horas_homens_trabalhadas
resultado = "Taxa de Frequência: {0}".format(taxa_frequencia)
#Para formatar o resultado com 2 casas decimais
#resultado = "Taxa de Frequência: {0:.2f}".format(taxa_frequencia)
print(resultado)