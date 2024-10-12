# _,-,_,-,_,-,_,-,_,-,_,-,_ MACRO DEFAULT RULES _,-,_,-,_,-,_,-,_,-,_,-,_ #
import os
import pyautogui
import time
from datetime import datetime
import keyboard
import cv2
import numpy as np

# LOGS
log_dir = r'data\logs'
os.makedirs(log_dir, exist_ok=True)

data_atual = datetime.now().strftime("%d-%m-%Y")
nome_arquivo_log = f'LOG_{data_atual}.txt'
caminho_log = os.path.join(log_dir, nome_arquivo_log)

log_file = open(caminho_log, 'a')

def log(msg, level='INFO'):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] [{level}] {msg}"
    print(log_message)
    log_file.write(log_message + '\n')

parar = False

def stop_macro():
    global parar
    log("Parando o macro...", level='INFO')
    parar = True
    
def verificar_interrupcao():
    if keyboard.is_pressed('esc'):
        log("Macro interrompida pelo usuário.", level='INFO')
        return True
    return False 

def detectar_aspecto_na_tela(imagem_modelo, threshold=0.8):
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    modelo = cv2.imread(imagem_modelo, cv2.IMREAD_COLOR)
    if modelo is None:
        log(f"Erro: a imagem modelo não pôde ser carregada de {imagem_modelo}. Verifique o caminho.")
        return None, None

    if len(modelo.shape) == 3 and modelo.shape[2] == 4:
        modelo = cv2.cvtColor(modelo, cv2.COLOR_BGRA2BGR)

    resultado = cv2.matchTemplate(screenshot, modelo, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    if max_val >= threshold:
        return max_loc, modelo.shape[:2]
    return None, None

def encontrar_imagem_e_clicar(imagem, descricao):
    posicao, tamanho = detectar_aspecto_na_tela(imagem)
    if posicao:
        centro_x = posicao[0] + tamanho[1] // 2
        centro_y = posicao[1] + tamanho[0] // 2
        pyautogui.moveTo(centro_x, centro_y)
        pyautogui.click()
        log(f"'{descricao}' encontrada e clicada.")
        return True
    return False

def encontrar_imagem_e_clicar_abaixo(imagem, descricao):
    posicao, tamanho = detectar_aspecto_na_tela(imagem)
    if posicao:
        centro_x = posicao[0] + tamanho[1] // 2
        centro_y = posicao[1] + tamanho[0] + 1
        pyautogui.moveTo(centro_x, centro_y)
        pyautogui.click()
        log(f"'{descricao}' encontrada e clicada abaixo da imagem.")
        return True
    return False

def verificar_reconectar(imagem_condicao, descricao):
    # imagem_condicao = r'data\server_down.png'
    posicao, tamanho = detectar_aspecto_na_tela(imagem_condicao)
    if posicao:
        centro_x = posicao[0] + tamanho[1] // 2
        centro_y = posicao[1] + tamanho[0] // 2
        pyautogui.moveTo(centro_x, centro_y)
        pyautogui.click()
        log(f"'{descricao}' encontrada e clicada. Reiniciando o processo.")
        return True
    return False

def macro_leaving_mission():
    log("Executando macro LEAVING MISSION...")
    for _ in range(4):
        pyautogui.press('esc')
        time.sleep(1.5)
    log("Macro LEAVING MISSION concluída.")
