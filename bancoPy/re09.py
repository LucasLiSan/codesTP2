# Em relação ao exercício anterior, crie um botão salvar , salve no banco de dados o nome do aluno, idade, e a media

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from pymongo import MongoClient

# ----- Conexão com MongoDB -----
# Altere a URI conforme seu ambiente (local ou remoto)
client = MongoClient("mongodb://localhost:27017/")  # para Mongo local padrão
db = client["escola_db"]
collection = db["alunos"]

# Função para calcular idade (opcional, se quiser armazenar idade)
def calcular_idade(data_nasc_str):
    nascimento = datetime.strptime(data_nasc_str, "%d/%m/%Y")
    hoje = datetime.today()
    idade = hoje.year - nascimento.year
    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1
    return idade

# Função para calcular média e definir situação
def calc_media(notas_list):
    soma = sum(notas_list)
    media = soma / len(notas_list)
    return media

def salvar_no_banco(nome, data_nasc, media):
    doc = {
        "nome": nome,
        "data_nascimento": data_nasc,
        "media": media
    }
    collection.insert_one(doc)
    # opcional: print ou log para confirmar
    print("Salvo:", doc)

# Função chamada quando clicar Calcular e exibir média
def calcular():
    nome = entry_nome.get().strip()
    data_nasc = entry_nascimento.get().strip()
    notas = []
    for e in entradas_notas:
        try:
            n = float(e.get())
        except:
            messagebox.showerror("Erro", "Notas inválidas!")
            return
        notas.append(n)
    if not nome or not data_nasc:
        messagebox.showerror("Erro", "Preencha nome e data de nascimento.")
        return

    # calcular média
    media = calc_media(notas)
    entry_media.delete(0, tk.END)
    entry_media.insert(0, f"{media:.2f}")

    # definir situação
    situacao = "APROVADO" if media >= 5 else "REPROVADO"
    label_situacao.config(text=f"Situação: {situacao}")

# Função chamada quando clicar SALVAR — salva no Mongo
def botao_salvar():
    nome = entry_nome.get().strip()
    data_nasc = entry_nascimento.get().strip()
    media_str = entry_media.get().strip()
    if not nome or not data_nasc or not media_str:
        messagebox.showerror("Erro", "Calcule a média antes de salvar.")
        return
    try:
        media = float(media_str)
    except:
        messagebox.showerror("Erro", "Média inválida.")
        return
    # salva
    salvar_no_banco(nome, data_nasc, media)
    messagebox.showinfo("Sucesso", "Aluno salvo no banco de dados!")

# ----- Interface Tkinter -----

janela = tk.Tk()
janela.title("Cadastro de Aluno")

tk.Label(janela, text="Nome do aluno:").pack()
entry_nome = tk.Entry(janela, width=30)
entry_nome.pack()

tk.Label(janela, text="Data de nascimento (DD/MM/AAAA):").pack()
entry_nascimento = tk.Entry(janela, width=15)
entry_nascimento.pack()

tk.Label(janela, text="Digite as 5 notas:").pack()
entradas_notas = []
for i in range(5):
    e = tk.Entry(janela, width=10)
    e.pack()
    entradas_notas.append(e)

tk.Button(janela, text="Calcular Média", command=calcular).pack(pady=5)
tk.Label(janela, text="Média:").pack()
entry_media = tk.Entry(janela, width=10)
entry_media.pack()

label_situacao = tk.Label(janela, text="Situação: ")
label_situacao.pack(pady=5)

tk.Button(janela, text="Salvar no Banco", command=botao_salvar).pack(pady=10)

janela.mainloop()
