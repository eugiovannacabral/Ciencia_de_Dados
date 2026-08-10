palavra = input("Digite uma palavra: ")
quant_vogal = 0
verificacao = False

for letra in palavra:
    print(letra.upper())
    print( )
    if(letra.lower() == 'a' or letra.lower() == 'e' or letra.lower() == 'i'or letra.lower() == 'u' ):
        quant_vogal +=1

    if(letra == 'a' or letra == 'A'):
        verificacao = True

print("Quantidade de vogais: ", quant_vogal)

if verificacao == True:
    print("A palavra possui a letra 'A' ")
else:
    print("A palavra não possui a letra 'A' ")

######questão 8 #######
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print("Adição: ", n1 + n2)
print("Subtração: ", n1 - n2)
print("Multiplicação: ", n1 * n2)
print("Divisão: ", n1 / n2)
print("Resto da divisão: ", n1 % n2)
print("Potência: ", n1 ** n2)