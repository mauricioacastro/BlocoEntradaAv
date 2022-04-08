# Função : Dados um valor de renda mensal total
# Autor : Maurício Castro
# Data : 07/04/2022

#Questão 03 - AT
#Crie um programa contendo uma função que, dados um valor de renda mensal total, gastos totais com moradia, gastos totais com educação e gastos totais com transporte, faça um diagnóstico da saúde financeira do usuário, com base nos valores percentuais acima expostos, informando qual é o percentual da renda mensal total comprometido por cada custo. 
#Se o gasto estiver dentro do percentual recomendado, informe ainda que
#Seus gastos estão dentro da margem recomendada.
#Caso contrário, informe:
#Portanto, idealmente, o máximo de sua renda comprometida com {tipo} deveria ser de R$ {valor_max}
#Onde tipo deve ser moradia, educação ou transportes e valor_max deve ser o valor equivalente ao percentual máximo de gasto com esse tipo de custo.

def imprimirGasto(tipo, percentualMaximo,gasto,renda):
    percentual=calcularPercentual(gasto,renda)
    msg = obterMensagem(gasto,renda,percentualMaximo,percentual)
    print(f"Seus gastos totais com {tipo} comprometem {percentual}% de sua renda total. O máximo recomendado é de {percentualMaximo}%. {msg}")

def calcularPercentual(gasto,renda):
    return gasto * 100 / renda

def calcularValorMaximo(renda,percentualMaximo):
    return renda * percentualMaximo / 100

def obterMensagem(gasto,renda,percentualMaximo,percentual):
    msg = "\nSeus gastos estão dentro da margem recomendada."
    if percentual > percentualMaximo:
        msg = f"\nPortanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {calcularValorMaximo(renda,percentualMaximo)}."
    return msg

percentualMaximoMoradia = 30
percentualMaximoEducacao = 20
percentualMaximoTransporte = 15

rendaMensal=float(input("Renda mensal total: R$"))
gastoMoradia=float(input("Gastos totais com moradia: R$"))
gastoEducacao=float(input("Gastos totais com educação: R$"))
gastoTransporte=float(input("Gastos totais com transporte: R$"))

print(30*"-")
print("        Diagnóstico")
print(30*"-")
imprimirGasto("moradia",percentualMaximoMoradia,gastoMoradia,rendaMensal)
print(30*"-")
imprimirGasto("educação",percentualMaximoEducacao,gastoEducacao,rendaMensal)
print(30*"-")
imprimirGasto("transporte",percentualMaximoTransporte,gastoTransporte,rendaMensal)
