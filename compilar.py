import os
import shutil
import subprocess

def compilar():
    script_principal = 'main.py'
    arquivo_icon = 'icon.png'

    subprocess.run(['pyinstaller', '--onefile', '--icon=' + arquivo_icon, script_principal])

    pasta_dist = 'dist'

    if os.path.exists(pasta_dist):
        shutil.copy(arquivo_icon, os.path.join(pasta_dist, arquivo_icon))
        print(f'{arquivo_icon} copiado para {pasta_dist}/')
    else:
        print('A pasta dist não foi encontrada.')
    
    if os.path.exists('data'):
        shutil.copytree('data', os.path.join(pasta_dist, 'data'))
        print("Pasta 'data' movida com sucesso!")

    print("Compilação concluída!")

if __name__ == "__main__":
    compilar()
