# Usando biblioteca Tkinter (Padrão Oython para Interface) 
import tkinter as tk

# Submódulo do Tkinter com widgets mais modernos e estilizados
from tkinter import ttk

def atualizar_resultado():
    # Obter o texto da caixa de entrada
    nome = caixa_texto.get()

    # Obter a opção selecionada nos botões de rádio
    preferencia = var_radio.get()

    # Verificar se a caixa de seleção de saudação informal está marcada
    if var_check_saudacao.get():
        saudacao = "Olá"
    else:
        saudacao = "Bem-vindo"

    # Verificar se a caixa de seleção de saudação personalizada está marcada
    if var_check_personalizada.get():
        saudacao = f"{saudacao}, caro(a)"

    # Obter a cor favorita selecionada
    cor_favorita = combo_cor.get()

    # Montar mensagem final
    mensagem = f"{saudacao} {nome} | Você prefere {preferencia}"
    if cor_favorita:
        mensagem += f"Sua cor favorita é {cor_favorita}."

    # Atualizar o texto do rótulo de mensagem
    label_resultado.config(text=mensagem)

#  criar a janela principal
janela = tk .Tk()
janela.title("Interface avançada")
janela.geometry("400x500")

# Mudando a cor de fundo da tela
janela.config(bg="light gray")

#  Criar uma caixa de entrada (Entry)
label_nome = tk.Label(janela, text="Digite seu nome: ", bg='yellow')
label_nome.pack(pady=5)
caixa_texto = tk.Entry(janela, width=40)
caixa_texto.pack(pady=5)

# Executar a janela principal
janela.mainloop()


