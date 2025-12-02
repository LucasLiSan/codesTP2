import tkinter as tk

# Funções da calculadora
expressao = ""

def adicionar_valor(valor):
    global expressao
    expressao += str(valor)
    label_resultado.config(text=expressao)

def limpar():
    global expressao
    expressao = ""
    label_resultado.config(text=expressao)

def calcular():
    global expressao
    try:
        resultado = eval(expressao)  # Calcula a expressão
        label_resultado.config(text=str(resultado))
        expressao = str(resultado)   # Permite continuar calculando com o resultado
    except:
        label_resultado.config(text="Erro")
        expressao = ""

# ---------------- Interface Tkinter ----------------

janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("300x400")

# Label para mostrar a expressão/resultados
label_resultado = tk.Label(janela, text="", anchor='e', bg="white", fg="black", height=2, font=("Arial", 20))
label_resultado.pack(fill="both")

# Frame para botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack()

# Botões da calculadora
botoes = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
]

for linha in botoes:
    frame_linha = tk.Frame(frame_botoes)
    frame_linha.pack(expand=True, fill="both")
    for b in linha:
        if b == "=":
            botao = tk.Button(frame_linha, text=b, width=5, height=2, font=("Arial", 15), command=calcular)
        else:
            botao = tk.Button(frame_linha, text=b, width=5, height=2, font=("Arial", 15), command=lambda valor=b: adicionar_valor(valor))
        botao.pack(side="left", expand=True, fill="both")

# Botão limpar separado
botao_limpar = tk.Button(janela, text="Limpar", bg="red", fg="white", font=("Arial", 15), command=limpar)
botao_limpar.pack(fill="both", expand=True)

janela.mainloop()
