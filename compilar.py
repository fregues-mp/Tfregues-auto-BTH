import os
import shutil
import subprocess

def compilar():
    # Nome do script principal
    script_principal = 'main.py'
    arquivo_icon = 'icon.ico'

    # Criação do executável usando PyInstaller
    subprocess.run(['pyinstaller', '--onefile', '--icon=' + arquivo_icon, script_principal])

    # Copia o arquivo icon.ico para a pasta dist
    pasta_dist = 'dist'

    # Verifica se a pasta dist existe
    if os.path.exists(pasta_dist):
        shutil.copy(arquivo_icon, os.path.join(pasta_dist, arquivo_icon))
        print(f'{arquivo_icon} copiado para {pasta_dist}/')
    else:
        print('A pasta dist não foi encontrada.')
    
    # Mover a pasta 'data' para o diretório de saída (onde o executável foi gerado)
    if os.path.exists('data'):
        shutil.copytree('data', os.path.join(pasta_dist, 'data'))
        print("Pasta 'data' movida com sucesso!")

    print("Compilação concluída!")

if __name__ == "__main__":
    compilar()
