# _,-,_,-,_,-,_,-,_,-,_,-,_ MACRO TO RUN MISSION _,-,_,-,_,-,_,-,_,-,_,-,_ #
import os
import pyautogui
import time
import keyboard
import numpy as np
import cv2
from datetime import datetime
from level0 import verificar_interrupcao, encontrar_imagem_e_clicar, macro_leaving_mission

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

def level1():
    while True:
        if verificar_interrupcao():
            break

        log("Iniciando sequência...")

        while not encontrar_imagem_e_clicar(r'data\level\level1\m1.png', 'Imagem 1'):
            if verificar_interrupcao():
                return
            log("Imagem 1 não encontrada. Tentando novamente...")
            time.sleep(1)

        while not encontrar_imagem_e_clicar(r'data\level\level1\m2.png', 'Imagem 2'):
            if verificar_interrupcao():
                return
            log("Imagem 2 não encontrada. Tentando novamente...")
            time.sleep(1)

        while not encontrar_imagem_e_clicar(r'data\level\level1\m3.png', 'Imagem 3'):
            if verificar_interrupcao():
                return
            log("Imagem 3 não encontrada. Tentando novamente...")
            time.sleep(1)

        log("Procurando por Imagem 4a...")
        while not encontrar_imagem_e_clicar(r'data\level\level1\m4a.png', 'Imagem 4a'):
            if verificar_interrupcao():
                return
            log("Imagem 4a não encontrada. Tentando novamente...")
            time.sleep(1)

        log("Procurando por Imagem 4b...")
        for _ in range(15):
            if verificar_interrupcao():
                return
            if encontrar_imagem_e_clicar(r'data\level\level1\m4b.png', 'Imagem 4b'):
                log("Imagem 4b encontrada. Executando macro LEAVING MISSION.")
                macro_leaving_mission()
                return

        while True:
            log("Procurando por Imagem 5a...")
            while not encontrar_imagem_e_clicar(r'data\level\level1\m5a.png', 'Imagem 5a'):
                if verificar_interrupcao():
                    return
                log("Imagem 5a não encontrada. Tentando novamente...")
                time.sleep(1)

            log("Procurando por Imagem 5b...")
            encontrada_5b = False
            for _ in range(30):
                if verificar_interrupcao():
                    return
                if encontrar_imagem_e_clicar(r'data\level\level1\m5b.png', 'Imagem 5b'):
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
        level1()
    finally:
        log_file.close()
