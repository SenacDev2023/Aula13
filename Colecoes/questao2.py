numeros = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

print("Os números em ordem inversa são:")
for i in range(len(numeros) - 1, -1, -1):
    print(numeros[i])