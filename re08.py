# Faça uma Interface Gráfica para Ler 5 notas , ler a idade do aluno e o nome do aluno e calcular média , verificar se o aluno está aprovado , se a nota for maior ou igual a 5 , reprovado abaixo de 5, mostre a média na caixa de texto, e no label a situação do aluno

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Vetor para armazenar notas
notas = []

# Matriz para armazenar vários alunos (nome, nascimento, idade, notas, média, situação)
alunos = []


# ---------------- FUNÇÃO PARA APLICAR MÁSCARA NA DATA ---------------- #
def mascara_data(event):
    texto = entry_nascimento.get()

    # Remove qualquer coisa que não seja dígito
    texto = ''.join([c for c in texto if c.isdigit()])

    # Aplica automaticamente DD/MM/AAAA
    novo = ""
    if len(texto) > 0:
        novo += texto[:2]
    if len(texto) > 2:
        novo += "/" + texto[2:4]
    if len(texto) > 4:
        novo += "/" + texto[4:8]

    entry_nascimento.delete(0, tk.END)
    entry_nascimento.insert(0, novo)


# ---------------- FUNÇÃO PARA CALCULAR IDADE ---------------- #
def calcular_idade(event=None):
    try:
        data_str = entry_nascimento.get()
        nascimento = datetime.strptime(data_str, "%d/%m/%Y")
        hoje = datetime.today()

        idade = hoje.year - nascimento.year
        if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
            idade -= 1

        label_idade.config(text=f"Idade: {idade} anos")
        return idade

    except:
        label_idade.config(text="Idade: inválida")
        return None


# ---------------- FUNÇÃO PARA CALCULAR MÉDIA ---------------- #
def calcular():
    notas.clear()

    nome = entry_nome.get()
    nascimento = entry_nascimento.get()

    idade = calcular_idade()  # calcula idade

    if nome == "" or idade is None:
        messagebox.showerror("Erro", "Verifique o nome e a data de nascimento!")
        return

    # Lê as 5 notas
    for i in range(5):
        nota = entradas_notas[i].get()
        if nota == "":
            messagebox.showerror("Erro", "Preencha todas as 5 notas!")
            return
        try:
            valor = float(nota)
        except:
            messagebox.showerror("Erro", "Digite notas válidas!")
            return

        notas.append(valor)

    # Cálculo da média
    soma = 0
    for n in notas:
        soma += n
    media = soma / len(notas)

    # Situação
    if media >= 5:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"

    entry_media.delete(0, tk.END)
    entry_media.insert(0, f"{media:.2f}")

    label_resultado.config(text=f"Situação: {situacao}")

    # Armazena na matriz
    alunos.append([nome, nascimento, idade, notas[:], media, situacao])


# --------------------------- INTERFACE GRÁFICA --------------------------- #

janela = tk.Tk()
janela.title("Sistema de Notas do Aluno")
janela.geometry("400x500")

# Nome
tk.Label(janela, text="Nome do aluno:").pack()
entry_nome = tk.Entry(janela, width=30)
entry_nome.pack()

# Data de nascimento com máscara
tk.Label(janela, text="Data de nascimento (DD/MM/AAAA):").pack()
entry_nascimento = tk.Entry(janela, width=15)
entry_nascimento.pack()

# Eventos: máscara ao digitar e cálculo da idade ao sair
entry_nascimento.bind("<KeyRelease>", mascara_data)
entry_nascimento.bind("<FocusOut>", calcular_idade)

# Label para exibir a idade
label_idade = tk.Label(janela, text="Idade: ")
label_idade.pack(pady=5)

# Notas
tk.Label(janela, text="Digite as 5 notas:").pack()

entradas_notas = []
for i in range(5):
    e = tk.Entry(janela, width=10)
    e.pack()
    entradas_notas.append(e)

# Botão calcular
tk.Button(janela, text="Calcular Média", command=calcular).pack(pady=10)

# Média
tk.Label(janela, text="Média do aluno:").pack()
entry_media = tk.Entry(janela, width=10)
entry_media.pack()

# Situação
label_resultado = tk.Label(janela, text="Situação:", font=("Arial", 12, "bold"))
label_resultado.pack(pady=10)

janela.mainloop()
