# Função : Eleitor
# Autor : Maurício Castro
# Data : 27/03/2022

#Em um concurso de fantasias, os jurados precisam digitar os nomes dos 5 participantes e suas respectivas notas, 
# variando de 0 até 10. Crie uma função que leia os nomes dos participantes e, ao final, apresente apenas o nome
# e a nota do vencedor.

#Fluxo de Exceção:
#o	O programa deve verificar se a nota da pessoa é maior ou igual a zero e menor ou igual a dez.


notaP1 = 0
notaP2 = 0
notaP3 = 0
notaP4 = 0
notaP5 = 0
notaVencedor = 0


participante1 = input("Informe nome do 1º participante: ")
notaP1 = float(input("Informe nota do 1º participante: "))
    
if notaP1 > notaVencedor:
    notaVencedor = notaP1
    vencedor = participante1 

participante2 = input("Informe nome do 2º participante: ")
notaP2 = float(input("Informe nota do 2º participante: "))
if notaP2 > notaVencedor:
    notaVencedor = notaP2
    vencedor = participante2 

participante3 = input("Informe nome do 3º participante: ")
notaP3 = float(input("Informe nota do 3º participante: "))
if notaP3 > notaVencedor:
    notaVencedor = notaP3
    vencedor = participante3 

participante4 = input("Informe nome do 4º participante: ")
notaP4 = float(input("Informe nota do 4º participante: "))
if notaP4 > notaVencedor:
    notaVencedor = notaP4
    vencedor = participante4 

participante5 = input("Informe nome do 5º participante: ")
notaP5 = float(input("Informe nota do 5º participante: "))
if notaP5 > notaVencedor:
    notaVencedor = notaP5
    vencedor = participante5 



print ("O vencedor(a) foi", vencedor,"com nota",notaVencedor,"!")