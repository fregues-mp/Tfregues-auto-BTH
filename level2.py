# _,-,_,-,_,-,_,-,_,-,_,-,_ MACRO TO RUN JXJ _,-,_,-,_,-,_,-,_,-,_,-,_ #
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

def run_level2():
    global parar
    level0.parar = False
    
    if level0.verificar_interrupcao():
        return
    if level0.parar == True:
        return

    log("Iniciando sequência...")

    # Encontrar Imagem 1 (j1)
    while not level0.encontrar_imagem_e_clicar(r'data\level\level2\j1.png', 'Imagem j1'):
        if level0.verificar_reconectar(r'data\level\level2\server_down.png', 'Server Down'):
            log("'Server Down' encontrada. Reiniciando o ciclo do início.")
            continue
        if level0.verificar_interrupcao():
            return
        if level0.parar == True:
            return
        log("Imagem j1 não encontrada. Tentando novamente...")
        time.sleep(1)

    # Encontrar Imagem 2 (j2)
    while not level0.encontrar_imagem_e_clicar(r'data\level\level2\j2.png', 'Imagem j2'):
        if level0.verificar_reconectar(r'data\level\level2\server_down.png', 'Server Down'):
            log("'Server Down' encontrada. Reiniciando o ciclo do início.")
            continue
        if level0.verificar_interrupcao():
            return
        if level0.parar == True:
            return
        log("Imagem j2 não encontrada. Tentando novamente...")
        time.sleep(1)

    # Encontrar Imagem 3 (j3)
    while not level0.encontrar_imagem_e_clicar(r'data\level\level2\j3.png', 'Imagem j3'):
        if level0.verificar_reconectar(r'data\level\level2\server_down.png', 'Server Down'):
            log("'Server Down' encontrada. Reiniciando o ciclo do início.")
            continue
        if level0.verificar_interrupcao():
            return
        if level0.parar == True:
            return
        log("Imagem j3 não encontrada. Tentando novamente...")
        time.sleep(1)

    # Encontrar Imagem 4 (j4)
    while not level0.encontrar_imagem_e_clicar(r'data\level\level2\j4.png', 'Imagem j4'):
        if level0.verificar_reconectar(r'data\level\level2\server_down.png', 'Server Down'):
            log("'Server Down' encontrada. Reiniciando o ciclo do início.")
            continue
        if level0.verificar_interrupcao():
            return
        if level0.parar == True:
            return
        log("Imagem j4 não encontrada. Tentando novamente...")
        time.sleep(1)

    # Encontrar Imagem 5 (j5)
    while not level0.encontrar_imagem_e_clicar(r'data\level\level2\j5.png', 'Imagem j5'):
        if level0.verificar_reconectar(r'data\level\level2\server_down.png', 'Server Down'):
            log("'Server Down' encontrada. Reiniciando o ciclo do início.")
            continue
        if level0.verificar_interrupcao():
            return
        if level0.parar == True:
            return
        log("Imagem j5 não encontrada. Tentando novamente...")
        time.sleep(1)

    log("Todos os níveis foram completados.")

if __name__ == "__main__":
    try:
        run_level2()
    finally:
        log_file.close()
