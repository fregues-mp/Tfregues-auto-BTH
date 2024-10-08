# _,-,_,-,_,-,_,-,_,-,_,-,_ SCRIPT TO RUN MISSION RAID _,-,_,-,_,-,_,-,_,-,_,-,_ #
import time
import pyautogui
import level0

def run_level4():
    global parar
    level0.parar = 0 False
    contador = 0

    if level0.verificar_interrupcao():
        return
    if level0.parar:
        return
    
    level0.log("Iniciando sequência...", level='INFO')

    # Encontrar Imagem 1
    while not level0.encontrar_imagem_e_clicar(r'data\level\level4\r1.png', 'Imagem 1'):
        if level0.verificar_reconectar(r'data\server_down.png', 'Server Down'):
            level0.log("'Server Down' encontrada.\nReniciando o ciclo do início.", level='WARNING')
            return
        if level0.verificar_interrupcao():
            return
        if level0.parar:
            return
        level0.log(f"Imagem 1 não encontrada.\nTentando novamente...({contador})", level='INFO')
        contador += 1

    contador = 0

    # Encontrar Imagem 2
    while not level0.encontrar_imagem_e_clicar(r'data\level\level4\r2.png', 'Imagem 2'):
        if level0.verificar_reconectar(r'data\server_down.png', 'Server Down'):
            level0.log("'Server Down' encontrada.\nReniciando o ciclo do início.", level='WARNING')
            return
        if level0.verificar_interrupcao():
            return
        if level0.parar:
            return
        level0.log(f"Imagem 2 não encontrada.\nTentando novamente...({contador})", level='INFO')
        contador += 1

    contador = 0

    # Encontrar Imagem 3
    while not level0.encontrar_imagem_e_clicar(r'data\level\level4\r3.png', 'Imagem 3'):
        if level0.verificar_reconectar(r'data\server_down.png', 'Server Down'):
            level0.log("'Server Down' encontrada.\nReniciando o ciclo do início.", level='WARNING')
            return
        if level0.verificar_interrupcao():
            return
        if level0.parar:
            return
        level0.log(f"Imagem 3 não encontrada.\nTentando novamente...({contador})", level='INFO')
        contador += 1

    contador = 0

    # Encontrar Imagem 4 ou 4v2
    while not level0.encontrar_imagem_e_clicar(r'data\level\level4\r4.png', 'Imagem 4'):
        if level0.encontrar_imagem_e_clicar(r'data\level\level4\r4v2', 'Imagem 4v2'):
            level0.log("O usuario não tem mais energia." level='INFO')
            break
        if level0.verificar_reconectar(r'data\server_down.png', 'Server Down'):
            level0.log("'Server Down' encontrada.\nReniciando o ciclo do início.", level='WARNING')
            return
        if level0.verificar_interrupcao():
            return
        if level0.parar:
            return
        level0.log(f"Imagem 4 não encontrada.\nTentando novamente...({contador})", level='INFO')
        contador += 1

    contador = 0

    # Encontrar Imagem 5
    while True:
        if level0.verificar_reconectar(r'data\server_down.png', 'Server Down'):
            level0.log("'Server Down' encontrada.\nReiniciando o ciclo do início.", level='WARNING')
            continue
        level0.log("Procurando por Imagem 5a..." level='INFO')
        while not level0.encontrar_imagem_e_clicar(r'data\level\level4\r5a', 'Imagem 5a'):
            if level0.verificar_reconectar

