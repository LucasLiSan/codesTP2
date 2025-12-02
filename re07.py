# Crie um vetor que leia valores inteiros , e mostre os valores armazenados , sem determinar a quantidade de números

valores = []
continuar = "s"

while continuar.lower() == "s":
    numero = int(input("Digite um número inteiro: "))
    valores.append(numero)

    continuar = input("Deseja adicionar outro número? (s/n): ")

print("\nValores armazenados no vetor:")
for v in valores:
    print(v)
