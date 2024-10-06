# _,-,_,-,_,-,_,-,_,-,_,-,_ SCRIPT TO RUN JXJ MACRO _,-,_,-,_,-,_,-,_,-,_,-,_ #
import time
import level0

def run_level2():
    global parar
    level0.parar = False

    if level0.verificar_interrupcao():
        return
    if level0.parar:
        return
    
    level0.log("Iniciando sequência...")

    # Encontrar Imagem 1
    while not level0.encontrar_imagem_e_clicar(r'data\level\level1\j1.png', 'Imagem 1'):
        if level0.verificar_reconectar(r'data\server_down.png', 'Server Down'):
            level0.log("'Server Down' encontrada. Reiniciando o ciclo do início.", level='WARNING')
            continue
        if level0.verificar_interrupcao():
            return
        if level0.parar:
            return
        level0.log("Imagem 1 não encontrada. Tentando novamente...", level='INFO')
        time.sleep(1)

    # Encontrar Imagem 2
    while not level0.encontrar_imagem_e_clicar(r'data\level\level2\j2.png', 'Imagem 2'):
        if level0.verificar_reconectar(r'data\server_down.png', 'Server Down'):
            level0.log("'Server Down' encontrada. Reniciando o ciclo do início.", level='INFO')
            continue
        if level0.verificar_interrupcao():
            return
        if level0.parar:
            return
        level0.log("Imagem 1 não encontrada. Tentando nomamente...", level='info')
        time.sleep(1)

    # Encontrar Imagem 3
    while True:
        if level0.encontrar_imagem_e_clicar_abaixo(r'data\level\level2\j3.png', 'Imagem 3'):
            level0.log("Imagem 3 encontrada. Continuando...", level='INFO')
            break
        elif level0.encontrar_imagem_e_clicar_abaixo(r'data\level\level2\j3v2.png', 'Imagem 3v2'):
            level0.log("Imagem 3v2 encontrada. Continuando...", level='INFO')
            break
        elif level0.verificar_reconectar(r'data\server_down.png', 'Server Down'):
            level0.log("'Server Down' encontrada. Reiniciando o ciclo do início.", level='WARNING')
            continue
        elif level0.verificar_interrupcao():
            return
        elif level0.parar:
            return

