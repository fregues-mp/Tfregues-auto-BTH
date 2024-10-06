# _,-,_,-,_,-,_,-,_,-,_,-,_ MACRO TO RUN MISSION _,-,_,-,_,-,_,-,_,-,_,-,_ #
import os
import time
import pyautogui
from datetime import datetime
import level0

# Criação do diretório de logs, se não existir
log_dir = r'data\logs'
os.makedirs(log_dir, exist_ok=True)

# Nome do arquivo de log com data
data_atual = datetime.now().strftime("%d-%m-%Y")
nome_arquivo_log = f'LOG_{data_atual}.txt'
caminho_log = os.path.join(log_dir, nome_arquivo_log)

# Redirecionar a saída padrão para o arquivo de log
log_file = open(caminho_log, 'a')

def log(msg):
    print(msg)
    log_file.write(msg + '\n')

def run_level1():
    global parar
    level0.parar = False
    
    if level0.verificar_interrupcao():
        return
    if level0.parar:
        return

    log("Iniciando sequência...")

    # Encontrar Imagem 1
    while not level0.encontrar_imagem_e_clicar(r'data\level\level1\m1.png', 'Imagem 1'):
        if level0.verificar_reconectar(r'data\level\level1\server_down.png', 'Server Down'):
            log("'Server Down' encontrada. Reiniciando o ciclo do início.")
            continue
        if level0.verificar_interrupcao():
            return
        if level0.parar:
            return
        log("Imagem 1 não encontrada. Tentando novamente...")
        time.sleep(1)

    # Encontrar Imagem 2
    while not level0.encontrar_imagem_e_clicar(r'data\level\level1\m2.png', 'Imagem 2'):
        if level0.verificar_reconectar(r'data\level\level1\server_down.png', 'Server Down'):
            log("'Server Down' encontrada. Reiniciando o ciclo do início.")
            continue
        if level0.verificar_interrupcao():
            return
        if level0.parar:
            return
        log("Imagem 2 não encontrada. Tentando novamente...")
        time.sleep(1)

    # Encontrar Imagem 3
    while True:
        if level0.encontrar_imagem_e_clicar(r'data\level\level1\m3.png', 'Imagem 3'):
            break  # Se a imagem 3 for encontrada, saia do loop
        elif level0.encontrar_imagem_e_clicar(r'data\level\level1\m3v2.png', 'Imagem 3v2'):
            log("Imagem 3v2 encontrada. Continuando...")
            break  # Se a imagem 3v2 for encontrada, saia do loop
        elif level0.verificar_reconectar(r'data\level\level1\server_down.png', 'Server Down'):
            log("'Server Down' encontrada. Reiniciando o ciclo do início.")
            continue  # Reinicie o ciclo se o servidor estiver fora
        elif level0.verificar_interrupcao():
            return  # Saia da função se uma interrupção for verificada
        elif level0.parar:
            return  # Saia da função se o macro estiver configurado para parar
        
        log("Imagem 3 não encontrada. Tentando novamente...")
        time.sleep(1)  # Aguarde um segundo antes de tentar novamente

    # Encontrar Imagem 4a
    log("Procurando por Imagem 4a...")
    while not level0.encontrar_imagem_e_clicar(r'data\level\level1\m4a.png', 'Imagem 4a'):
        if level0.verificar_reconectar(r'data\level\level1\server_down.png', 'Server Down'):
            log("'Server Down' encontrada. Reiniciando o ciclo do início.")
            continue
        if level0.verificar_interrupcao():
            return
        if level0.parar:
            return
        log("Imagem 4a não encontrada. Tentando novamente...")
        time.sleep(1)

    # Encontrar Imagem 4b
    log("Procurando por Imagem 4b...")
    for _ in range(1):
        if level0.verificar_reconectar(r'data\level\level1\server_down.png', 'Server Down'):
            log("'Server Down' encontrada. Reiniciando o ciclo do início.")
            continue
        if level0.verificar_interrupcao():
            return
        if level0.parar:
            return
        if level0.encontrar_imagem_e_clicar(r'data\level\level1\m4b.png', 'Imagem 4b'):
            log("Imagem 4b encontrada. Executando macro LEAVING MISSION.")
            level0.macro_leaving_mission()
            return

    # Encontrar Imagem 5a e 5b
    while True:
        if level0.verificar_reconectar(r'data\level\level1\server_down.png', 'Server Down'):
            log("'Server Down' encontrada. Reiniciando o ciclo do início.")
            continue
        log("Procurando por Imagem 5a...")
        while not level0.encontrar_imagem_e_clicar(r'data\level\level1\m5a.png', 'Imagem 5a'):
            if level0.verificar_reconectar(r'data\level\level1\server_down.png', 'Server Down'):
                log("'Server Down' encontrada. Reiniciando o ciclo do início.")
                continue
            if level0.verificar_interrupcao():
                return
            if level0.parar:
                return
            log("Imagem 5a não encontrada. Tentando novamente...")
            time.sleep(1)

        log("Procurando por Imagem 5b...")
        encontrada_5b = False
        for _ in range(1):
            if level0.verificar_reconectar(r'data\level\level1\server_down.png', 'Server Down'):
                log("'Server Down' encontrada. Reiniciando o ciclo do início.")
                continue
            if level0.verificar_interrupcao():
                return
            if level0.parar:
                return
            if level0.encontrar_imagem_e_clicar(r'data\level\level1\m5b.png', 'Imagem 5b'):
                log("Imagem 5b encontrada. Clicando ESC uma vez.")
                pyautogui.press('esc')
                encontrada_5b = True
                break

        if not encontrada_5b:
            log("Imagem 5b não encontrada. Retornando à busca pela Imagem 5a.")
        else:
            break

if __name__ == "__main__":
    try:
        run_level1()
    finally:
        log_file.close()
