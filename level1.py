import time
import pyautogui
import level0

def run_level1():
    global parar
    level0.parar = False

    if level0.verificar_interrupcao():
        return
    if level0.parar:
        return

    level0.log("Iniciando sequência...")

    # Encontrar Imagem 1
    while not level0.encontrar_imagem_e_clicar(r'data\level\level1\m1.png', 'Imagem 1'):
        if level0.verificar_reconectar(r'data\level\level1\server_down.png', 'Server Down'):
            level0.log("'Server Down' encontrada. Reiniciando o ciclo do início.", level='WARNING')
            continue
        if level0.verificar_interrupcao():
            return
        if level0.parar:
            return
        level0.log("Imagem 1 não encontrada. Tentando novamente...")
        time.sleep(1)

    # Encontrar Imagem 2
    while not level0.encontrar_imagem_e_clicar(r'data\level\level1\m2.png', 'Imagem 2'):
        if level0.verificar_reconectar(r'data\level\level1\server_down.png', 'Server Down'):
            level0.log("'Server Down' encontrada. Reiniciando o ciclo do início.", level='WARNING')
            continue
        if level0.verificar_interrupcao():
            return
        if level0.parar:
            return
        level0.log("Imagem 2 não encontrada. Tentando novamente...")
        time.sleep(1)

    # Encontrar Imagem 3
    while True:
        if level0.encontrar_imagem_e_clicar(r'data\level\level1\m3.png', 'Imagem 3'):
            break
        elif level0.encontrar_imagem_e_clicar(r'data\level\level1\m3v2.png', 'Imagem 3v2'):
            level0.log("Imagem 3v2 encontrada. Continuando...")
            break
        elif level0.verificar_reconectar(r'data\level\level1\server_down.png', 'Server Down'):
            level0.log("'Server Down' encontrada. Reiniciando o ciclo do início.", level='WARNING')
            continue
        elif level0.verificar_interrupcao():
            return
        elif level0.parar:
            return
        
        level0.log("Imagem 3 não encontrada. Tentando novamente...")
        time.sleep(1)  # Aguarde um segundo antes de tentar novamente

    # Encontrar Imagem 4a
    level0.log("Procurando por Imagem 4a...")
    while not level0.encontrar_imagem_e_clicar(r'data\level\level1\m4a.png', 'Imagem 4a'):
        if level0.verificar_reconectar(r'data\level\level1\server_down.png', 'Server Down'):
            level0.log("'Server Down' encontrada. Reiniciando o ciclo do início.", level='WARNING')
            continue
        if level0.verificar_interrupcao():
            return
        if level0.parar:
            return
        level0.log("Imagem 4a não encontrada. Tentando novamente...")
        time.sleep(1)

    # Encontrar Imagem 4b
    level0.log("Procurando por Imagem 4b...")
    for _ in range(1):
        if level0.verificar_reconectar(r'data\level\level1\server_down.png', 'Server Down'):
            level0.log("'Server Down' encontrada. Reiniciando o ciclo do início.", level='WARNING')
            continue
        if level0.verificar_interrupcao():
            return
        if level0.parar:
            return
        if level0.encontrar_imagem_e_clicar(r'data\level\level1\m4b.png', 'Imagem 4b'):
            level0.log("Imagem 4b encontrada. Executando macro LEAVING MISSION.")
            level0.macro_leaving_mission()
            return

    # Encontrar Imagem 5a e 5b
    while True:
        if level0.verificar_reconectar(r'data\level\level1\server_down.png', 'Server Down'):
            level0.log("'Server Down' encontrada. Reiniciando o ciclo do início.", level='WARNING')
            continue
        level0.log("Procurando por Imagem 5a...")
        while not level0.encontrar_imagem_e_clicar(r'data\level\level1\m5a.png', 'Imagem 5a'):
            if level0.verificar_reconectar(r'data\level\level1\server_down.png', 'Server Down'):
                level0.log("'Server Down' encontrada. Reiniciando o ciclo do início.", level='WARNING')
                continue
            if level0.verificar_interrupcao():
                return
            if level0.parar:
                return
            level0.log("Imagem 5a não encontrada. Tentando novamente...")
            time.sleep(1)

        level0.log("Procurando por Imagem 5b...")
        encontrada_5b = False
        for _ in range(1):
            if level0.verificar_reconectar(r'data\level\level1\server_down.png', 'Server Down'):
                level0.log("'Server Down' encontrada. Reiniciando o ciclo do início.", level='WARNING')
                continue
            if level0.verificar_interrupcao():
                return
            if level0.parar:
                return
            if level0.encontrar_imagem_e_clicar(r'data\level\level1\m5b.png', 'Imagem 5b'):
                level0.log("Imagem 5b encontrada. Clicando ESC uma vez.")
                pyautogui.press('esc')
                encontrada_5b = True
                break

        if not encontrada_5b:
            level0.log("Imagem 5b não encontrada. Retornando à busca pela Imagem 5a.")
        else:
            break

if __name__ == "__main__":
    try:
        run_level1()
    finally:
        level0.log_file.close()
