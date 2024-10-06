import os
import shutil

def compilar():
    # Compilar o main.py com PyInstaller
    os.system('pyinstaller --onefile --noconsole --icon=icon.ico --add-data "data;data" main.py')

    # Mover a pasta 'data' para o diretório de saída (onde o executável foi gerado)
    output_dir = os.path.join('dist')
    if os.path.exists('data'):
        shutil.copytree('data', os.path.join(output_dir, 'data'))
        print("Pasta 'data' movida com sucesso!")

    print("Compilação concluída!")

if __name__ == "__main__":
    compilar()
