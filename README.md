# Tfregues-auto-BTH

Este é um macro para o jogo *Bit Heroes*, desenvolvido pelo fregues com o objetivo de facilitar o jogo ao máximo. Ainda estou trabalhando nele e muitas mudanças podem ser feitas no futuro. Atualmente, o macro utiliza um método de detecção de imagens para realizar o *afkfarm*, tornando-o útil para deixar rodando enquanto você dorme.



## Arquivos

- **data**: Contém as imagens e recursos necessários para o funcionamento do macro.
- **logs**: Armazena os registros das atividades realizadas pelo macro, permitindo monitorar o desempenho e identificar possíveis problemas.
- **level0.py**: Contém funções comuns usadas por outros arquivos do macro.
- **level1.py**: Implementa a lógica principal para a execução do macro, focando nas missões.
- **main.py**: O ponto de entrada do programa, onde a execução do macro é iniciada.

Futuramente, planejamos adicionar os macros `level2`, `level3`, `level4`, `level5`, e `level6`.

## Considerações

O arquivo `level1.py`, responsável por automatizar as missões, ainda não está 100% completo. Na seleção de fases, não consegui incluir todas as opções. Enquanto isso, você pode ir até `data\level\level1` e trocar a imagem `m2` pela fase que deseja jogar. Recomendo o uso do Lightshot para capturar as imagens.
exemplo:

![m2](https://github.com/user-attachments/assets/95392baf-6313-4640-bd8a-a125bf0ba589) ![m2b](https://github.com/user-attachments/assets/c02adeff-acad-41db-bda0-06ce5db8d23c) ![m2c](https://github.com/user-attachments/assets/a677a861-27c8-4d58-8e85-6d828d4b41ec)

No momento, o macro está configurado apenas para missões.

Ainda estou desenvolvendo uma interface gráfica (GUI) usando a biblioteca Pygame.

No futuro, irei adicionar as funcionalidades para Missões, PvP, Boss, Raid, Expedição, Coliseu e Pesca.

 
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
	pyinstaller --onefile --noconsole --icon=icon.ico --add-data "data;data" main.py
	```
	

## Contribuições

Sinta-se à vontade para contribuir! Abra um issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License.
