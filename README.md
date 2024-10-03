# Tfregues-auto-BTH

Este é um macro para o jogo *Bit Heroes*, desenvolvido com o objetivo de facilitar o jogo ao máximo. Ainda estou trabalhando nele e muitas mudanças podem ser feitas no futuro. Atualmente, o macro utiliza um método de detecção de imagens para realizar o *afkfarm*, tornando-o útil para deixar rodando enquanto você dorme.

No momento, o macro está configurado apenas para missões, mas estou desenvolvendo uma interface gráfica (GUI) usando a biblioteca Pygame. No futuro, planejo adicionar funcionalidades para Missões, PvP, Boss, Raid, Expedição, Coliseu e Pesca.

## Arquivos

- **level0.py**: Contém funções comuns usadas por outros arquivos do macro.
- **level1.py**: Implementa a lógica principal para a execução do macro, focando nas missões.
- **main.py**: O ponto de entrada do programa, onde a execução do macro é iniciada.

Futuramente, planejamos adicionar os macros `level2`, `level3`, `level4`, `level5`, e `level6`.

## Executando

1. Clone o repositório:
	```bash
	git clone https://github.com/rafaelitoto895/Tfregues-auto-BTH.git
	```
2. Instale as dependências necessárias:
	```bash
	pip install opencv-python numpy pyautogui pygame
	```
3. Execute o macro com o seguinte comando:
	```bash
	python main.py
	```
   
## Compilando
	
1. certifique-se que as dependências estão instaladas:
	```bash
	pip install opencv-python numpy pyautogui pygame pyinstaller
	```
2. compile o projeto em um unico arquivo:
	```bash
	pyinstaller --onefile --icon=icon.ico --add-data "data;data" main.py
	```
	

## Contribuições

Sinta-se à vontade para contribuir! Abra um issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License.


pyinstaller --onefile --icon=icon.ico --add-data "data;data" main.py
