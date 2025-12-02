# Crie vetor para ler 6 nomes de animais mostre os animais armazenadas no vetor

animais = []

for i in range(6):
    nome = input(f"Digite o nome do animal {i+1}: ")
    animais.append(nome)

print("\nAnimais armazenados no vetor:")
for animal in animais:
    print(animal)
    