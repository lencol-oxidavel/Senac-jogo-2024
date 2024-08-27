import tkinter as tk
from random import choice
from tkinter import messagebox

# Função que inicia o jogo
def start(jogador):
    # Dicionário de escolhas
    escolhas = {'Pedra': 'pe', 'Papel': 'pa', 'Tesoura': 'te'}
    jogador_escolha = escolhas[jogador]
    computador_escolha = choice(['pe', 'pa', 'te'])

    # Determina o resultado do jogo
    resultado = ""
    if jogador_escolha == computador_escolha:
        resultado = 'Empate'
    elif (jogador_escolha == 'pe' and computador_escolha == 'te') or \
         (jogador_escolha == 'pa' and computador_escolha == 'pe') or \
         (jogador_escolha == 'te' and computador_escolha == 'pa'):
        resultado = 'Vitória'
    else:
        resultado = 'Derrota'

    # Exibe o resultado em uma caixa de mensagem
    messagebox.showinfo("Resultado", f"Você escolheu: {jogador}\nComputador escolheu: {computador_escolha}\n\n{resultado}")

# Função chamada ao clicar em um botão
def clique_botao(jogador):
    start(jogador)

# Cria a janela principal
root = tk.Tk()
root.title("Pedra, Papel e Tesoura")

# Define o tamanho da janela (largura x altura)
largura_janela = 300
altura_janela = 200

# Calcula a posição para centralizar a janela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)

# Define a geometria da janela com a posição calculada
root.geometry("{}x{}+{}+{}".format(largura_janela, altura_janela, pos_x, pos_y))

# Cria os botões
botao_pedra = tk.Button(root, text="Pedra", command=lambda: clique_botao("Pedra"))
botao_papel = tk.Button(root, text="Papel", command=lambda: clique_botao("Papel"))
botao_tesoura = tk.Button(root, text="Tesoura", command=lambda: clique_botao("Tesoura"))

# Posiciona os botões na janela
botao_pedra.pack(side=tk.LEFT, padx=10, pady=10)
botao_papel.pack(side=tk.LEFT, padx=10, pady=10)
botao_tesoura.pack(side=tk.LEFT, padx=10, pady=10)

# Inicia o loop principal da interface gráfica
root.mainloop()
