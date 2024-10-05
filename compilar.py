import os
import shutil
import subprocess

# Caminhos
script_principal = 'main.py'
data_dir = 'data'
output_dir = 'dist'

def compilar():
    print("Iniciando a compilação com PyInstaller...")
    comando = [
        'pyinstaller',
        '--onefile',
        '--icon=icon.ico',
        '--add-data', f'{data_dir};{data_dir}',  # Inclui o diretório data
        script_principal
    ]
    subprocess.run(comando)
    print("Compilação concluída!")

def mover_data():
    caminho_destino = os.path.join(output_dir, script_principal.replace('.py', ''))

    if not os.path.exists(caminho_destino):
        print(f"Erro: O diretório {caminho_destino} não existe. Verifique se a compilação foi bem-sucedida.")
        return

    shutil.copytree(data_dir, os.path.join(caminho_destino, data_dir), dirs_exist_ok=True)
    print(f"Diretório '{data_dir}' movido para {caminho_destino} com sucesso!")

def main():
    compilar()
    mover_data()

if __name__ == '__main__':
    main()
