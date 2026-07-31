import math


distancia = int(input("Qual é a distância percorrida pela sua viagem(km) : "))

if(distancia <= 200):
    print ("O preco da passagem será R$ ", 0.50 * distancia)
elif(distancia > 200):
    print ("O preco da passagem será R$ ", 0.45 * distancia)

#########questão 5#########

numero = int(input("Digite um número de 1000 até 99999: "))

while numero < 1000 or numero > 9999:
    numero = int(input("Digite um número de 1000 até 99999: "))

numero = str(numero)
print('O número da unidade é: ', numero[3])
print('O número da dezena é: ', numero[2])
print('O número da centena é: ', numero[1])
print('O número do milhar é: ', numero[0])

#######questão 6 ########
numero = float(input("Digite um número decimal : "))
print("A raiz quadrada : ", math.sqrt(numero))
print("Arrendondado para cima : ", math.ceil(numero))
print("Arrendondado para baixo : ", math.floor(numero))
print("Parte inteira : ", math.trunc(numero))





