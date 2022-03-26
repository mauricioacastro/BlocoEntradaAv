# Função : Calcule a divisão de uma conta de bar 
# Autor : Maurício Castro
# Data : 26/03/2022

#Fluxo de exceção:
#O programa deve verificar se o número total de pessoas é maior do que zero.
#O programa deve verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100. 
#Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro “Valor inválido” e 
#o programa deve ser interrompido.

totalConsumo = 0
totalConta = 0
contaPessoa = 0
pessoas = 0
servico = 0

totalConsumo = str(input("Informe o valor total do consumo:"))
pessoas = int(input("Informe o total de pessoas:"))
servico = int(input("Informe o percentual do serviço, entre 0 e 100:"))
print ("O valor total da conta, com a taxa de serviço, será de R$",totalConsumo.replace('.', ','))
print ("Dividindo a conta por ",pessoas," pessoa(s), cada pessoa deverá pagar R$",contaPessoa)
