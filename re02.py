# Calcule a área de um terreno , leia o comprimento e a largura , e calcule a área = comprimento * largura , mostre o valor da área do terreno

# 1. Código básico
comprimento = float(input("Digite o comprimento do terreno (em metros): "))
largura = float(input("Digite a largura do terreno (em metros): "))

area = comprimento * largura

print(f"A área do terreno é: {area:.2f} m²")

#2. Versão usando while (calcular vários terrenos)
continuar = "s"

while continuar.lower() == "s":
    comprimento = float(input("Digite o comprimento do terreno: "))
    largura = float(input("Digite a largura do terreno: "))

    area = comprimento * largura
    print(f"A área do terreno é: {area:.2f} m²")

    continuar = input("Deseja calcular outro terreno? (s/n): ")

#3. Versão usando vetor (lista de terrenos) Armazena comprimentos, larguras e áreas.

comprimentos = []
larguras = []
areas = []

n = int(input("Quantos terrenos deseja cadastrar? "))

for i in range(n):
    comp = float(input(f"Comprimento do terreno {i+1}: "))
    larg = float(input(f"Largura do terreno {i+1}: "))

    comprimentos.append(comp)
    larguras.append(larg)
    areas.append(comp * larg)

print("\nÁreas dos terrenos:")
for i in range(n):
    print(f"Terreno {i+1}: {areas[i]:.2f} m²")

#4. Versão usando matriz (cada linha = um terreno) Formato da matriz: [comprimento, largura, area]

n = int(input("Quantos terrenos deseja cadastrar? "))

matriz = []

for i in range(n):
    comprimento = float(input(f"Comprimento do terreno {i+1}: "))
    largura = float(input(f"Largura do terreno {i+1}: "))
    area = comprimento * largura

    matriz.append([comprimento, largura, area])

print("\nTabela de terrenos:")
for i in range(n):
    print(f"Terreno {i+1} - Comprimento: {matriz[i][0]} m | Largura: {matriz[i][1]} m | Área: {matriz[i][2]:.2f} m²")