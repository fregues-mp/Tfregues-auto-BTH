# _,-,_,-,_,-,_,-,_,-,_,-,_ MACRO DEFAULT RULES _,-,_,-,_,-,_,-,_,-,_,-,_ #
import pyautogui
import time
import keyboard
import cv2
import numpy as np
import threading

parar = False

def stop_macro():
    # Para o macro pela GUI
    global parar
    print("Parando o macro...")
    parar = True
    
def verificar_interrupcao():
    # Verifica se a tecla 'esc' foi pressionada.
    if keyboard.is_pressed('esc'):
        print("Macro interrompida pelo usuário.")
        return True
    return False 

def detectar_aspecto_na_tela(imagem_modelo, threshold=0.8):
    # Detecta a presença de uma imagem modelo na tela.
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    modelo = cv2.imread(imagem_modelo, cv2.IMREAD_COLOR)
    if modelo is None:
        print(f"Erro: a imagem modelo não pôde ser carregada de {imagem_modelo}. Verifique o caminho.")
        return None, None

    if len(modelo.shape) == 3 and modelo.shape[2] == 4:
        modelo = cv2.cvtColor(modelo, cv2.COLOR_BGRA2BGR)

    resultado = cv2.matchTemplate(screenshot, modelo, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    if max_val >= threshold:
        return max_loc, modelo.shape[:2]
    return None, None

def encontrar_imagem_e_clicar(imagem, descricao):
    # Encontra uma imagem na tela e clica nela.
    posicao, tamanho = detectar_aspecto_na_tela(imagem)
    if posicao:
        centro_x = posicao[0] + tamanho[1] // 2
        centro_y = posicao[1] + tamanho[0] // 2
        pyautogui.moveTo(centro_x, centro_y)
        pyautogui.click()
        print(f"'{descricao}' encontrada e clicada.")
        return True
    return False

def verificar_reconectar(imagem_condicao, descricao):
    # Verifica a condição de reconexão e clica se a imagem for encontrada.
    posicao, tamanho = detectar_aspecto_na_tela(imagem_condicao)
    if posicao:
        centro_x = posicao[0] + tamanho[1] // 2
        centro_y = posicao[1] + tamanho[0] // 2
        pyautogui.moveTo(centro_x, centro_y)
        pyautogui.click()
        print(f"'{descricao}' encontrada e clicada. Reiniciando o processo.")
        return True
    return False

def macro_leaving_mission():
    # Executa a macro para deixar a missão.
    print("Executando macro LEAVING MISSION...")
    for _ in range(4):
        pyautogui.press('esc')
        time.sleep(1.5)
    print("Macro LEAVING MISSION concluída.")