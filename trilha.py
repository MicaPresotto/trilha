import sys    ##Importando o módulo sys para contribuir com o código

##Definindo as variáveis
inicio = input("Tecle ENTER para começar ou digite SAIR para sair! ").upper()
pecas = 1
vez = '\u29bf'
pecasJog1 = 9
pecasJog2 = 9

##Definindo as casas do tabuleiro com unicodes representando as posições
casas = [['\u24b6', '\u24b7', '\u24b8'],
         ['\u24b9', '\u24ba', '\u24bb'],
         ['\u24bc', '\u24bd', '\u24be'],
         ['\u24bf', '\u24c0', '\u24c1', '\u24c2', '\u24c3', '\u24c4'],
         ['\u24c5', '\u24c6', '\u24c7'],
         ['\u24c8', '\u24c9', '\u24ca'],
         ['\u24cb', '\u24cc', '\u24cd']]

##Ideia que não deu muito certo mas por falta de tempo
trilha = {'ABC':False, 'DEF':False, 'GHI':False, 'JKL':False, 'MNO':False, 'PQR':False, 'STU':False, 'VWX':False, 'AJV':False, 'DKS':False, 'GLP':False, 'BEH':False, 'QTW':False, 'IMR':False, 'FNU':False, 'COX':False}

##Função para printar as regras ao jogador
def regras():
    print('REGRAS:')
    print('O jogo de Trilha tem dois participantes, que usam um tabuleiro para jogar.')
    print('Jogadores - 2')
    print('Peças - 18 peças sendo 9 brancas e 9 pretas.')
    print('Tabuleiro - tabuleiro com 24 casa interligados horizontalmente e verticalmente.')
    print('Objetivo - Deixar o adversário com 2 peças no tabuleiro ou deixá-lo sem movimentos.')
    print()
    print('O jogo termina quando uma dentre três situações são alcançadas:')
    print('- Se um jogador reduzir as peças de seu adversário para 2.\n- Se um jogador deixar seu adversário sem nenhuma jogada válida. Caso seu adversário tenha somente 3 peças em jogo, ele não poderá ser "trancado".\n- Se ambos jogadores estiverem com 3 peças em jogo e, a partir deste momento, se em 10 jogadas não houver vencedor, o jogo terminará e será declarado um empate.')
    print()
    print("Durante a movimentação das peças, você poderá apenas movimentá-las por onde há um caminho('=' ou '||').")


##Função para printar o tabuleiro e as peças 
def tabuleiro(casas):
    print((' %s ================  %s  ================ %s\n') % (casas[0][0], casas[0][1], casas[0][2]),
    ('||                             ||                             ||\n'),
    ('||         %s ========= %s ========= %s         ||\n') % (casas[1][0], casas[1][1], casas[1][2]),
    ('||         ||                 ||                 ||         ||\n'),
    ('||         ||       %s === %s === %s       ||         ||\n') % (casas[2][0], casas[2][1], casas[2][2]),
    ('||         ||       ||        -        ||       ||         ||\n'),
    ('%s ==== %s === %s                 %s === %s ==== %s\n') % (casas[3][0], casas[3][1], casas[3][2], casas[3][3], casas[3][4], casas[3][5]),
    ('||         ||       ||        -        ||       ||         ||\n'),
    ('||         ||       %s === %s === %s       ||         ||\n') % (casas[4][0], casas[4][1], casas[4][2]),
    ('||         ||                 ||                 ||         ||\n'),
    ('||         %s ========= %s ========= %s         ||\n') % (casas[5][0], casas[5][1], casas[5][2]),
    ('||                             ||                             ||\n'),
    ('%s ================  %s  ================ %s\n') % (casas[6][0], casas[6][1], casas[6][2]))

##Função para verificar se a casa já está ocupada e colocar a peça respectiva de cada jogador        
def confereCasa(casas):
    global pecas, vez, jogada
    if (jogada == 'A' and casas[0][0] != 'A') or \
       (jogada == 'B' and casas[0][1] != 'B') or \
       (jogada == 'C' and casas[0][2] != 'C') or \
       (jogada == 'D' and casas[1][0] != 'D') or \
       (jogada == 'E' and casas[1][1] != 'E') or \
       (jogada == 'F' and casas[1][2] != 'F') or \
       (jogada == 'G' and casas[2][0] != 'G') or \
       (jogada == 'H' and casas[2][1] != 'H') or \
       (jogada == 'I' and casas[2][2] != 'I') or \
       (jogada == 'J' and casas[3][0] != 'J') or \
       (jogada == 'K' and casas[3][1] != 'K') or \
       (jogada == 'L' and casas[3][2] != 'L') or \
       (jogada == 'M' and casas[3][3] != 'M') or \
       (jogada == 'N' and casas[3][4] != 'N') or \
       (jogada == 'O' and casas[3][5] != 'O') or \
       (jogada == 'P' and casas[4][0] != 'P') or \
       (jogada == 'Q' and casas[4][1] != 'Q') or \
       (jogada == 'R' and casas[4][2] != 'R') or \
       (jogada == 'S' and casas[5][0] != 'S') or \
       (jogada == 'T' and casas[5][1] != 'T') or \
       (jogada == 'U' and casas[5][2] != 'U') or \
       (jogada == 'V' and casas[6][0] != 'V') or \
       (jogada == 'W' and casas[6][1] != 'W') or \
       (jogada == 'X' and casas[6][2] != 'X') :
        if jogada == 'A':
            if casas[0][0] == '\u24b6':        
                casas[0][0] = vez
            else:
                vez = vez
                return False
        elif jogada == 'B':
            if casas[0][1] == '\u24b7':
                casas[0][1] = vez
            else:
                vez = vez
                return False
        elif jogada == 'C':
            if casas[0][2] == '\u24b8':
                casas[0][2] = vez
            else:
                vez = vez
                return False
        elif jogada == 'D':
            if casas[1][0] == '\u24b9':
                casas[1][0] = vez
            else:
                vez = vez
                return False
        elif jogada == 'E':
            if casas[1][1] == '\u24ba':
                casas[1][1] = vez
            else:
                vez = vez
                return False
        elif jogada == 'F':
            if casas[1][2] == '\u24bb':
                casas[1][2] = vez
            else:
                vez = vez
                return False
        elif jogada == 'G':
            if casas[2][0] == '\u24bc':
                casas[2][0] = vez
            else:
                vez = vez
                return False
        elif jogada == 'H':
            if casas[2][1] == '\u24bd':
                casas[2][1] = vez
            else:
                vez = vez
                return False
        elif jogada == 'I':
            if casas[2][2] == '\u24be':
                casas[2][2] = vez
            else:
                vez = vez
                return False
        elif jogada == 'J':
            if casas[3][0] == '\u24bf':
                casas[3][0] = vez
            else:
                vez = vez
                return False
        elif jogada == 'K':
            if casas[3][1] == '\u24c0':
                casas[3][1] = vez
            else:
                vez = vez
                return False
        elif jogada == 'L':
            if casas[3][2] == '\u24c1':
                casas[3][2] = vez
            else:
                vez = vez
                return False
        elif jogada == 'M':
            if casas[3][3] == '\u24c2':
                casas[3][3] = vez
            else:
                vez = vez
                return False
        elif jogada == 'N':
            if casas[3][4] == '\u24c3':
                casas[3][4] = vez
            else:
                vez = vez
                return False
        elif jogada == 'O':
            if casas[3][5] == '\u24c4':
                casas[3][5] = vez
            else:
                vez = vez
                return False
        elif jogada == 'P':
            if casas[4][0] == '\u24c5':
                casas[4][0] = vez
            else:
                vez = vez
                return False
        elif jogada == 'Q':
            if casas[4][1] == '\u24c6':
                casas[4][1] = vez
            else:
                vez = vez
                return False
        elif jogada == 'R':
            if casas[4][2] == '\u24c7':
                casas[4][2] = vez
            else:
                vez = vez
                return False
        elif jogada == 'S':
            if casas[5][0] == '\u24c8':
                casas[5][0] = vez
            else:
                vez = vez
                return False
        elif jogada == 'T':
            if casas[5][1] == '\u24c9':
                casas[5][1] = vez
            else:
                vez = vez
                return False
        elif jogada == 'U':
            if casas[5][2] == '\u24ca':
                casas[5][2] = vez
            else:
                vez = vez
                return False
        elif jogada == 'V':
            if casas[6][0] == '\u24cb':
                casas[6][0] = vez
            else:
                vez = vez
                return False
        elif jogada == 'W':
            if casas[6][1] == '\u24cc':
                casas[6][1] = vez
            else:
                vez = vez
                return False
        elif jogada == 'X':
            if casas[6][2] == '\u24cd':
                casas[6][2] = vez
            else:
                vez = vez
                return False
        return True
    else:
        pecas = pecas
        print('Movimento Inválido!')
        return False

##Função para conferir se o jogador fez uma trilha
def confereTrilha(casas, trilha):
    global pecasJog1, pecasJog2, vez
    if casas[0][0] == casas[0][1] == casas[0][2] == vez or \
       casas[1][0] == casas[1][1] == casas[1][2] == vez or \
       casas[2][0] == casas[2][1] == casas[2][2] == vez or \
       casas[3][0] == casas[3][1] == casas[3][2] == vez or \
       casas[3][3] == casas[3][4] == casas[3][5] == vez or \
       casas[4][0] == casas[4][1] == casas[4][2] == vez or \
       casas[5][0] == casas[5][1] == casas[5][2] == vez or \
       casas[6][0] == casas[6][1] == casas[6][2] == vez or \
       casas[0][0] == casas[3][0] == casas[6][0] == vez or \
       casas[1][0] == casas[3][1] == casas[5][0] == vez or \
       casas[2][0] == casas[3][2] == casas[4][0] == vez or \
       casas[0][1] == casas[1][1] == casas[2][1] == vez or \
       casas[4][1] == casas[5][1] == casas[6][1] == vez or \
       casas[2][2] == casas[3][3] == casas[4][2] == vez or \
       casas[1][2] == casas[3][4] == casas[5][2] == vez or \
       casas[0][2] == casas[3][5] == casas[6][2] == vez:
        if casas[0][0] == casas[0][1] == casas[0][2]:
            if trilha['ABC'] == False:
                removedor_dePecas(casas)
                trilha['ABC'] = true_orFalse(trilha['ABC'])
            return True
        elif casas[1][0] == casas[1][1] == casas[1][2]:
            if trilha['DEF'] == False:
                removedor_dePecas(casas)
                trilha['DEF'] = true_orFalse(trilha['DEF'])
            return True
        elif casas[2][0] == casas[2][1] == casas[2][2]:
            if trilha['GHI'] == False:
                removedor_dePecas(casas)
                trilha['GHI'] = true_orFalse(trilha['GHI'])
            return True
        elif casas[3][0] == casas[3][1] == casas[3][2]:
            if trilha['JKL'] == False:
                removedor_dePecas(casas)
                trilha['JKL'] = true_orFalse(trilha['JKL'])
            return True
        elif casas[3][3] == casas[3][4] == casas[3][5]:
            if trilha['MNO'] == False:
                removedor_dePecas(casas)
                trilha['MNO'] = true_orFalse(trilha['MNO'])
            return True
        elif casas[4][0] == casas[4][1] == casas[4][2]:
            if trilha['PQR'] == False:
                removedor_dePecas(casas)
                trilha['PQR'] = true_orFalse(trilha['PQR'])
            return True
        elif casas[5][0] == casas[5][1] == casas[5][2]:
            if trilha['STU'] == False:
                removedor_dePecas(casas)
                trilha['STU'] = true_orFalse(trilha['STU'])
            return True
        elif casas[6][0] == casas[6][1] == casas[6][2]:
            if trilha['VWX'] == False:
                removedor_dePecas(casas)
                trilha['VWX'] = true_orFalse(trilha['VWX'])
            return True
        elif casas[0][0] == casas[3][0] == casas[6][0]:
            if trilha['AJV'] == False:
                removedor_dePecas(casas)
                trilha['AJV'] = true_orFalse(trilha['AJV'])
            return True
        elif casas[1][0] == casas[3][1] == casas[5][0]:
            if trilha['DKS'] == False:
                removedor_dePecas(casas)
                trilha['DKS'] = true_orFalse(trilha['DKS'])
            return True
        elif casas[2][0] == casas[3][2] == casas[4][0]:
            if trilha['GLP'] == False:
                removedor_dePecas(casas)
                trilha['GLP'] = true_orFalse(trilha['GLP'])
            return True
        elif casas[0][1] == casas[1][1] == casas[2][1]:
            if trilha['BEH'] == False:
                removedor_dePecas(casas)
                trilha['BEH'] = true_orFalse(trilha['BEH'])
            return True
        elif casas[4][1] == casas[5][1] == casas[6][1]:
            if trilha['QTW'] == False:
                removedor_dePecas(casas)
                trilha['QTW'] = true_orFalse(trilha['QTW'])
            return True
        elif casas[2][2] == casas[3][3] == casas[4][2]:
            if trilha['IMR'] == False:
                removedor_dePecas(casas)
                trilha['IMR'] = true_orFalse(trilha['IMR'])
            return True
        elif casas[1][2] == casas[3][4] == casas[5][2]:
            if trilha['FNU'] == False:
                removedor_dePecas(casas)
                trilha['FNU'] = true_orFalse(trilha['FNU'])
            return True
        elif casas[0][2] == casas[3][5] == casas[6][2]:
            if trilha['COX'] == False:
                removedor_dePecas(casas)
                trilha['COX'] = true_orFalse(trilha['COX'])
            return True
        return False
        
##Função para remover as peças do adversário caso haja uma trilha
def removedor_dePecas(casas):
    global vez, pecasJog1, pecasJog2
    if vez == '\u29bf':
        vez = '\u29be'
        removePeca = input("VOCÊ %s  FEZ UMA TRILHA! Escolha uma peça adversária para remover: "%vez).upper()
        troca_Vez()
    else:
        vez = '\u29bf'
        removePeca = input("VOCÊ %s  FEZ UMA TRILHA! Escolha uma peça adversária para remover: "%vez).upper()
        troca_Vez()
    while removePeca != 'A' and \
        removePeca != 'B' and \
        removePeca != 'C' and \
        removePeca != 'D' and \
        removePeca != 'E' and \
        removePeca != 'F' and \
        removePeca != 'G' and \
        removePeca != 'H' and \
        removePeca != 'I' and \
        removePeca != 'J' and \
        removePeca != 'K' and \
        removePeca != 'L' and \
        removePeca != 'M' and \
        removePeca != 'N' and \
        removePeca != 'O' and \
        removePeca != 'P' and \
        removePeca != 'Q' and \
        removePeca != 'R' and \
        removePeca != 'S' and \
        removePeca != 'T' and \
        removePeca != 'U' and \
        removePeca != 'V' and \
        removePeca != 'W' and \
        removePeca != 'X':
        removePeca = input("DADO INVÁLIDO! Escolha uma peça adversária para remover: ").upper()
    if vez == '\u29be':
        pecasJog2 -= 1
    elif vez == '\u29bf':
        pecasJog1 -= 1  
    if removePeca == 'A':
        if casas[0][0] == "\u29be":
            casas[0][0] = '\u24b6'
        elif casas[0][0] == "\u29bf":
            casas[0][0] = '\u24b6'  
    elif removePeca == 'B':
        if casas[0][1] == "\u29be":
            casas[0][1] = '\u24b7'
        elif casas[0][1] == "\u29bf":
            casas[0][1] = '\u24b7'  
    elif removePeca == 'C':
        if casas[0][2] == "\u29be":
            casas[0][2] = '\u24b8'
        elif casas[0][2] == "\u29bf":
            casas[0][2] = '\u24b8'     
    elif removePeca == 'D':
        if casas[1][0] == "\u29be":
            casas[1][0] = '\u24b9'
        elif casas[1][0] == "\u29bf":
            casas[1][0] = '\u24b9'  
    elif removePeca == 'E':
        if casas[1][1] == "\u29be":
            casas[1][1] = '\u24ba'
        elif casas[1][1] == "\u29bf":
            casas[1][1] = '\u24ba'  
    elif removePeca == 'F':
        if casas[1][2] == "\u29be":
            casas[1][2] = '\u24bb'
        elif casas[1][2] == "\u29bf":
            casas[1][2] = '\u24bb'  
    elif removePeca == 'G':
        if casas[2][0] == "\u29be":
            casas[2][0] = '\u24bc'
        elif casas[2][0] == "\u29bf":
            casas[2][0] = '\u24bc'
    elif removePeca == 'H':
        if casas[2][1] == "\u29be":
            casas[2][1] = '\u24bd'
        elif casas[2][1] == "\u29bf":
            casas[2][1] = '\u24bd'  
    elif removePeca == 'I':
        if casas[2][2] == "\u29be":
            casas[2][2] = '\u24be'
        elif casas[2][2] == "\u29bf":
            casas[2][2] = '\u24be'  
    elif removePeca == 'J':
        if casas[3][0] == "\u29be":
            casas[3][0] = '\u24bf'
        elif casas[3][0] == "\u29bf":
            casas[3][0] = '\u24bf'  
    elif removePeca == 'K':
        if casas[3][1] == "\u29be":
            casas[3][1] = '\u24c0'
        elif casas[3][1] == "\u29bf":
            casas[3][1] = '\u24c0'  
    elif removePeca == 'L':
        if casas[3][2] == "\u29be":
            casas[3][2] = '\u24c1'
        elif casas[3][2] == "\u29bf":
            casas[3][2] = '\u24c1'  
    elif removePeca == 'M':
        if casas[3][3] == "\u29be":
            casas[3][3] = '\u24c2'
        elif casas[3][3] == "\u29bf":
            casas[3][3] = '\u24c2'  
    elif removePeca == 'N':
        if casas[3][4] == "\u29be":
            casas[3][4] = '\u24c3'
        elif casas[3][4] == "\u29bf":
            casas[3][4] = '\u24c3'  
    elif removePeca == 'O':
        if casas[3][5] == "\u29be":
            casas[3][5] = '\u24c4'
        elif casas[3][5] == "\u29bf":
            casas[3][5] = '\u24c4'  
    elif removePeca == 'P':
        if casas[4][0] == "\u29be":
            casas[4][0] = '\u24c5'
        elif casas[4][0] == "\u29bf":
            casas[4][0] = '\u24c5'  
    elif removePeca == 'Q':
        if casas[4][1] == "\u29be":
            casas[4][1] = '\u24c6'
        elif casas[4][1] == "\u29bf":
            casas[4][1] = '\u24c6'  
    elif removePeca == 'R':
        if casas[4][2] == "\u29be":
            casas[4][2] = '\u24c7'
        elif casas[4][2] == "\u29bf":
            casas[4][2] = '\u24c7'  
    elif removePeca == 'S':
        if casas[5][0] == "\u29be":
            casas[5][0] = '\u24c8'
        elif casas[5][0] == "\u29bf":
            casas[5][0] = '\u24c8'  
    elif removePeca == 'T':
        if casas[5][1] == "\u29be":
            casas[5][1] = '\u24c9'
        elif casas[5][1] == "\u29bf":
            casas[5][1] = '\u24c9'  
    elif removePeca == 'U':
        if casas[5][2] == "\u29be":
            casas[5][2] = '\u24ca'
        elif casas[5][2] == "\u29bf":
            casas[5][2] = '\u24ca'  
    elif removePeca == 'V':
        if casas[6][0] == "\u29be":
            casas[6][0] = '\u24cb'
        elif casas[6][0] == "\u29bf":
            casas[6][0] = '\u24cb'  
    elif removePeca == 'W':
        if casas[6][1] == "\u29be":
            casas[6][1] = '\u24cc'
        elif casas[6][1] == "\u29bf":
            casas[6][1] = '\u24cc'  
    elif removePeca == 'X':
        if casas[6][2] == "\u29be":
            casas[6][2] = '\u24cd'
        elif casas[6][2] == "\u29bf":
            casas[6][2] = '\u24cd'
    print()  
    return tabuleiro(casas)

##Função para modificar a condição booleana da trilha feita(parte da ideia inicial)
def true_orFalse(condicao):
    if condicao == True:
        condicao = False
    else:
        condicao = True

##Outra função que faz parte da ideia inicial 
def sei_la():
    global casas, vez, trilha
    if casas[0][0] != casas[0][1] != casas[0][2]:
        trilha['ABC'] = False
    if casas[1][0] != casas[1][1] != casas[1][2]:
        trilha['DEF'] = False
    if casas[2][0] != casas[2][1] != casas[2][2]:
        trilha['GHI'] = False
    if casas[3][0] != casas[3][1] != casas[3][2]:
        trilha['JKL'] = False
    if casas[3][3] != casas[3][4] != casas[3][5]:
        trilha['MNO'] = False
    if casas[4][0] != casas[4][1] != casas[4][2]:
        trilha['PQR'] = False
    if casas[5][0] != casas[5][1] != casas[5][2]:
        trilha['STU'] = False
    if casas[6][0] != casas[6][1] != casas[6][2]:
        trilha['VWX'] = False
    if casas[0][0] != casas[3][0] != casas[6][0]:
        trilha['AJV'] = False
    if casas[1][0] != casas[3][1] != casas[5][0]:
        trilha['DKS'] = False
    if casas[2][0] != casas[3][2] != casas[4][0]:
        trilha['GLP'] = False
    if casas[0][1] != casas[1][1] != casas[2][1]:
        trilha['BEH'] = False
    if casas[4][1] != casas[5][1] != casas[6][1]:
        trilha['QTW'] = False
    if casas[2][2] != casas[3][3] != casas[4][2]:
        trilha['IMR'] = False
    if casas[1][2] != casas[3][4] != casas[5][2]:
        trilha['FNU'] = False
    if casas[0][2] != casas[3][5] != casas[6][2]:
        trilha['COX'] = False
    return trilha

##Função para trocar as vezes dos jogadores
def troca_Vez():
    global vez
    if vez == '\u29bf':
        vez = '\u29be'
    else:
        vez = '\u29bf'
    print()
    print('Agora é a vez de', vez)
    return vez

##Função para movimentar as peças dos jogadores, pedindo a peça que você quer mover e para que posição
def movimentoPecas(casas):
    global vez
    dQual = input("De que posição você deseja mover sua peça? ").upper()       ##Qual peça você deseja mover
    while dQual != 'A' and \
        dQual != 'B' and \
        dQual != 'C' and \
        dQual != 'D' and \
        dQual != 'E' and \
        dQual != 'F' and \
        dQual != 'G' and \
        dQual != 'H' and \
        dQual != 'I' and \
        dQual != 'J' and \
        dQual != 'K' and \
        dQual != 'L' and \
        dQual != 'M' and \
        dQual != 'N' and \
        dQual != 'O' and \
        dQual != 'P' and \
        dQual != 'Q' and \
        dQual != 'R' and \
        dQual != 'S' and \
        dQual != 'T' and \
        dQual != 'U' and \
        dQual != 'V' and \
        dQual != 'W' and \
        dQual != 'X':
        dQual = input("DADO INVÁLIDO! De que posição você deseja mover sua peça? ")
    if dQual == 'A':
        casas[0][0] = '\u24b6'
    elif dQual == 'B':
        casas[0][1] = '\u24b7'
    elif dQual == 'C':
        casas[0][2] = '\u24b8'
    elif dQual == 'D':
        casas[1][0] = '\u24b9'
    elif dQual == 'E':
        casas[1][1] = '\u24ba'
    elif dQual == 'F':
        casas[1][2] = '\u24bb'
    elif dQual == 'G':
        casas[2][0] = '\u24bc'
    elif dQual == 'H':
        casas[2][1] = '\u24bd'
    elif dQual == 'I':
        casas[2][2] = '\u24be'
    elif dQual == 'J':
        casas[3][0] = '\u24bf'
    elif dQual == 'K':
        casas[3][1] = '\u24c0'
    elif dQual == 'L':
        casas[3][2] = '\u24c1'
    elif dQual == 'M':
        casas[3][3] = '\u24c2'
    elif dQual == 'N':
        casas[3][4] = '\u24c3'
    elif dQual == 'O':
        casas[3][5] = '\u24c4'
    elif dQual == 'P':
        casas[4][0] = '\u24c5'
    elif dQual == 'Q':
        casas[4][1] = '\u24c6'
    elif dQual == 'R':
        casas[4][2] = '\u24c7'
    elif dQual == 'S':
        casas[5][0] = '\u24c8'
    elif dQual == 'T':
        casas[5][1] = '\u24c9'
    elif dQual == 'U':
        casas[5][2] = '\u24ca'
    elif dQual == 'V':
        casas[6][0] = '\u24cb'
    elif dQual == 'W':
        casas[6][1] = '\u24cc'
    elif dQual == 'X':
        casas[6][2] = '\u24cd'
    confereCasa(casas)
    pQual = input("Para qual posição você deseja mover sua peça? ").upper()              ##Para onde deseja mover
    while pQual != 'A' and \
        pQual != 'B' and \
        pQual != 'C' and \
        pQual != 'D' and \
        pQual != 'E' and \
        pQual != 'F' and \
        pQual != 'G' and \
        pQual != 'H' and \
        pQual != 'I' and \
        pQual != 'J' and \
        pQual != 'K' and \
        pQual != 'L' and \
        pQual != 'M' and \
        pQual != 'N' and \
        pQual != 'O' and \
        pQual != 'P' and \
        pQual != 'Q' and \
        pQual != 'R' and \
        pQual != 'S' and \
        pQual != 'T' and \
        pQual != 'U' and \
        pQual != 'V' and \
        pQual != 'W' and \
        pQual != 'X':
        pQual = input("DADO INVÁLIDO! De que posição você deseja mover sua peça? ")
    if pQual == 'A':
        if dQual == 'B' or dQual == 'J':
            casas[0][0] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'B':
        if dQual == 'A' or dQual == 'C' or dQual == 'E':
            casas[0][1] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'C':
        if dQual == 'B' or dQual == 'O':
            casas[0][2] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'D':
        if dQual == 'L' or dQual == 'E':
            casas[1][0] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'E':
        if dQual == 'D' or dQual == 'F' or dQual == 'B' or dQual == 'H':
            casas[1][1] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'F':
        if dQual == 'E' or dQual == 'N':
            casas[1][2] = vez
            troca_Vez()
        else:
            dQual = vez
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'G':
        if dQual == 'L' or dQual == 'H':
            casas[2][0] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'H':
        if dQual == 'G' or dQual == 'I' or dQual == 'E':
            casas[2][1] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'I':        
        if dQual == 'M' or dQual == 'H':
            casas[2][2] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'J':
        if dQual == 'A' or dQual == 'K' or dQual == 'V':
            casas[3][0] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'K':        
        if dQual == 'D' or dQual == 'L' or dQual == 'J' or dQual == 'S':
            casas[3][1] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'L':        
        if dQual == 'K' or dQual == 'G' or dQual == 'P':
            casas[3][2] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'M':        
        if dQual == 'I' or dQual == 'R' or dQual == 'N':
            casas[3][3] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'N':        
        if dQual == 'M' or dQual == 'F' or dQual == 'U' or dQual == 'O':
            casas[3][4] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'O':
        if dQual == 'C' or dQual == 'X' or dQual == 'N':
            casas[3][5] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'P':
        if dQual == 'L' or dQual == 'Q':
            casas[4][0] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'Q':        
        if dQual == 'P' or dQual == 'R' or dQual == 'T':
            casas[4][1] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'R':        
        if dQual == 'M' or dQual == 'Q':
            casas[4][2] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'S':
        if dQual == 'K' or dQual == 'T':
            casas[5][0] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'T':        
        if dQual == 'S' or dQual == 'Q' or dQual == 'U' or dQual == 'W':
            casas[5][1] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'U':        
        if dQual == 'N' or dQual == 'T':
            casas[5][2] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'V':        
        if dQual == 'J' or dQual == 'W':
            casas[6][0] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'W':        
        if dQual == 'V' or dQual == 'X' or dQual == 'T':
            casas[6][1] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    elif pQual == 'X':        
        if dQual == 'W' or dQual == 'O':
            casas[6][2] = vez
            troca_Vez()
        else:
            print('JOGADA INVÁLIDA!')
            vez = vez
            print('A vez continua de', vez)
            dontSkip(dQual, casas)
    tabuleiro(casas)

##Função para corrigir o movimento das posições
def dontSkip(dQual, casas):
    if dQual == 'A':
        casas[0][0] = vez
    elif dQual == 'B':
        casas[0][1] = vez
    elif dQual == 'C':
        casas[0][2] = vez
    elif dQual == 'D':
        casas[1][0] = vez
    elif dQual == 'E':
        casas[1][1] = vez
    elif dQual == 'F':
        casas[1][2] = vez            
    elif dQual == 'G':
        casas[2][0] = vez
    elif dQual == 'H':
        casas[2][1] = vez
    elif dQual == 'I':
        casas[2][2] = vez
    elif dQual == 'J':
        casas[3][0] = vez
    elif dQual == 'K':
        casas[3][1] = vez
    elif dQual == 'L':
        casas[3][2] = vez
    elif dQual == 'M':
        casas[3][3] = vez
    elif dQual == 'N':
        casas[3][4] = vez
    elif dQual == 'O':
        casas[3][5] = vez
    elif dQual == 'P':
        casas[4][0] = vez
    elif dQual == 'Q':
        casas[4][1] = vez            
    elif dQual == 'R':
        casas[4][2] = vez
    elif dQual == 'S':
        casas[5][0] = vez
    elif dQual == 'T':
        casas[5][1] = vez
    elif dQual == 'U':
        casas[5][2] = vez
    elif dQual == 'V':
        casas[6][0] = vez
    elif dQual == 'W':
        casas[6][1] = vez
    elif dQual == 'X':
        casas[6][2] = vez
    confereCasa(casas)
    confereTrilha(casas, trilha)
    ganhador()
    tabuleiro(casas)

##Função para identificar se houve ganhador
def ganhador():
    if pecasJog1 < 3 or pecasJog2 < 3:
        print('O jogo terminou. Um dos jogadores está com peças insuficientes.')
        inicio = input("Se você deseja jogar novamente digite 'Y'(YES). Se não, digite 'N'(NO): ").upper()
        while inicio != 'Y' and inicio != 'N':
            inicio = input("DADO INVÁLIDO! Se você deseja jogar novamente digite 'Y'(YES). Se não, digite 'N'(NO): ").upper()
    else:
        pass

##Começando a jogar
while inicio == '':
    print()
    regras() ##Printando as regras
    print()
    print('O jogador com as peças %s  vai começar.'% vez)  ##Qual jogador irá começar a partida
    tabuleiro(casas)       ##Chamada da função para printar o tabuleiro
    while pecas <= 18:
        jogada = input("Escolha sua casa: ").upper()     ##Escolhendo a posição da peça
        while jogada != 'A' and \
              jogada != 'B' and \
              jogada != 'C' and \
              jogada != 'D' and \
              jogada != 'E' and \
              jogada != 'F' and \
              jogada != 'G' and \
              jogada != 'H' and \
              jogada != 'I' and \
              jogada != 'J' and \
              jogada != 'K' and \
              jogada != 'L' and \
              jogada != 'M' and \
              jogada != 'N' and \
              jogada != 'O' and \
              jogada != 'P' and \
              jogada != 'Q' and \
              jogada != 'R' and \
              jogada != 'S' and \
              jogada != 'T' and \
              jogada != 'U' and \
              jogada != 'V' and \
              jogada != 'W' and \
              jogada != 'X':
            jogada = input("DADO INVÁLIDO! Escolha sua casa: ").upper()
        if confereCasa(casas) == True:
            troca_Vez()
            pecas += 1
        else:
            print('MOVIMENTO INVÁLIDO!')
            print('A vez continua de', vez)
            pecas = pecas
            confereCasa(casas)
        tabuleiro(casas)
        confereTrilha(casas, trilha)
        sei_la()
        ganhador()
    
    print()
    print('CHEGOU A HORA DE MOVIMENTAR AS PEÇAS.')
    print()
    while pecasJog1 >=3  or pecasJog2 >= 3:
        movimentoPecas(casas)
##        sei_la()
        confereTrilha(casas, trilha)
        if trilha['ABC'] != True and \
            trilha['GHI'] != True and \
            trilha['JKL'] != True and \
            trilha['MNO'] != True and \
            trilha['PQR'] != True and \
            trilha['STU'] != True and \
            trilha['VWX'] != True and \
            trilha['AJV'] != True and \
            trilha['DKS'] != True and \
            trilha['GLP'] != True and \
            trilha['BEH'] != True and \
            trilha['QTW'] != True and \
            trilha['IMR'] != True and \
            trilha['FNU'] != True and \
            trilha['COX'] != True:
##            confereTrilha(casas, trilha)
            sei_la()
        else:
            pass 
        ganhador()
else:
    print('Obrigado por jogar!')
    print('Saindo...')
    print('F')
    sys.exit()