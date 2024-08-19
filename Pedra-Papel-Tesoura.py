from random import choice


def start():
    jogador = str(input("Selecione uma opção: 'pe' para pedra, 'pa' para papel e 'te' para tesoura"))
    # método choice do módulo random
    computador = choice(['te', 'pa', 'pe'])

    # se a escolha do jogoador for a mesma da maquina então é um empate
    if jogador == computador:
        return 'empate'
    # pe > te, te > pa, pa > pe
    # pedra vence tesoura, tesoura vence papel, papel vence pedra
    elif jogador != 'pe' or 'pa' or 'te':
        return 'selecione uma opção valida'
        # se o escrever algo que não está nas opções
    elif (jogador == 'te' and computador == 'pa' or jogador == 'pe' and computador == 'te' or jogador == 'pa' and
          computador == 'pe'):
        return 'vitória'

    # se nenhuma das condições acima forem satisfeitas então só sobra a derrota
    return 'Derrota'


print(start())
