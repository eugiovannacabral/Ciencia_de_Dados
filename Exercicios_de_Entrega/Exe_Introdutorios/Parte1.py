nome_completo = input("Digite seu nome completo : ")

print(nome_completo.upper())
print(nome_completo.lower())
print(len(nome_completo))
print (nome_completo.replace('De mesuita','do Inatel'))


vetor = nome_completo.split()
quantidade = len(nome_completo.split())

for n in range(0, quantidade):
    vetor[-1] = "do Inatel"

for palavras in vetor:
    print(palavras, end=' ')

print ()

########## questão 2 ########
numero_tabuada = int(input("De qual número você deseja saber a tabuada? "))
inicio = int(input("De onde deseja que comece a tabuada ? "))
fim = int(input("De onde deseja que termine a tabuada ? "))

for n in range(inicio, fim+1):
    print(n, "x", numero_tabuada, "=", n * numero_tabuada)

########## questão 3 ########
sexo = ' '

while sexo != "M" and sexo != "F" :
    sexo = input("Digite seu sexo(M ou F) : ")
    if sexo == "F" :
        print("Mulher")
    elif sexo == "M" :
        print("Homem")
    else:
        print("Inválido!")