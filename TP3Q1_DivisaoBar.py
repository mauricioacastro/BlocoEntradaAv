# Função : Calcule a divisão de uma conta de bar 
# Autor : Maurício Castro
# Data : 26/03/2022

totalConsumo = 0
totalConta = 0
contaPessoa = 0
pessoas = 0
servico = 0

totalConsumo = float(input("Informe o valor total do consumo:"))
pessoas = int(input("Informe o total de pessoas:")) #deve ser maior que 0
servico = int(input("Informe o percentual do serviço, entre 0 e 100:")) 
#verificar se é valido, entre 0 e 100
#Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro “Valor inválido” e 
#o programa deve ser interrompido.

totalConta = totalConsumo + (totalConsumo * servico / 100)
contaPessoa = totalConta / pessoas

print ("O valor total da conta, com a taxa de serviço, será de R$", totalConta )#.replace('.', ','))
print ("Dividindo a conta por ",pessoas," pessoa(s), cada pessoa deverá pagar R$",contaPessoa)
