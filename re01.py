# Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%. Elabore um algoritmo que leia o valor da compra e mostre o valor de venda para o produto.

#1. Versão básica (somente if)
valor_compra = float(input("Digite o valor da compra: "))

if valor_compra < 20:
    valor_venda = valor_compra * 1.45
else:
    valor_venda = valor_compra * 1.30

print(f"Valor de venda: R$ {valor_venda:.2f}")

#2. Versão usando while (várias compras)
continuar = "s"

while continuar.lower() == "s":
    valor_compra = float(input("Digite o valor da compra: "))

    if valor_compra < 20:
        valor_venda = valor_compra * 1.45
    else:
        valor_venda = valor_compra * 1.30

    print(f"Valor de venda: R$ {valor_venda:.2f}")

    continuar = input("Deseja calcular outro produto? (s/n): ")

#3. Versão usando vetor (lista) de compras
compras = []
vendas = []

n = int(input("Quantos produtos deseja cadastrar? "))

for i in range(n):
    valor = float(input(f"Valor de compra do produto {i+1}: "))
    compras.append(valor)

for valor_compra in compras:
    if valor_compra < 20:
        vendas.append(valor_compra * 1.45)
    else:
        vendas.append(valor_compra * 1.30)

print("\nValores de venda:")
for i in range(n):
    print(f"Produto {i+1}: R$ {vendas[i]:.2f}")

#4. Versão usando matriz (tabela de produtos) Cada linha terá: [valor_compra, valor_venda]

n = int(input("Quantos produtos deseja cadastrar? "))

matriz = []

for i in range(n):
    valor_compra = float(input(f"Valor de compra do produto {i+1}: "))

    if valor_compra < 20:
        valor_venda = valor_compra * 1.45
    else:
        valor_venda = valor_compra * 1.30

    matriz.append([valor_compra, valor_venda])

print("\nTabela de compras e vendas:")
for i in range(n):
    print(f"Produto {i+1} - Compra: R$ {matriz[i][0]:.2f} | Venda: R$ {matriz[i][1]:.2f}")

