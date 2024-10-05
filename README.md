# Tfregues-auto-BTH

Este é um macro para o jogo *Bit Heroes*, desenvolvido pelo fregues com o objetivo de facilitar o jogo ao máximo. Ainda estou trabalhando nele e muitas mudanças podem ser feitas no futuro. Atualmente, o macro utiliza um método de detecção de imagens para realizar o *AFKFARM*, tornando-o útil para deixar rodando enquanto você dorme.


## Funcionalidades
- **Detecção automática de imagens**: O macro usa um sistema de reconhecimento de imagem para identificar e clicar automaticamente nos elementos da interface do jogo.
- **AFK Farming**: Configure o macro para jogar por você enquanto realiza outras atividades.
- **Reconexão automática**: Caso o servidor do jogo caia, o macro detecta e realiza o procedimento de reconexão automaticamente.
- **Controle por GUI**: O macro possui uma interface gráfica desenvolvida com Pygame, facilitando seu uso e controle(ainda em desenvolvimento).
- **Suporte ao idioma PT-BR**: O macro está totalmente em português, com previsão de suporte para inglês no futuro.

## Arquivos do Projeto

- **/data**: Contém as imagens e recursos necessários para o funcionamento do macro.
- **/logs**: Armazena registros de execução, permitindo monitoramento do desempenho.
- **[level0.py](https://github.com/rafaelitoto895/Tfregues-auto-BTH/blob/main/level0.py)**: Arquivo com funções comuns usadas pelos diferentes níveis do macro.
- **[level1.py](https://github.com/rafaelitoto895/Tfregues-auto-BTH/blob/main/level1.py)**: Lógica principal do primeiro nível do macro, responsável por automatizar as missões.
- **[main.py](https://github.com/rafaelitoto895/Tfregues-auto-BTH/blob/main/main.py)**: Arquivo principal que inicializa a interface gráfica e o controle do macro.

- **[compilar.py](https://github.com/rafaelitoto895/Tfregues-auto-BTH/blob/main/compilar.py)**: Script que automatiza o processo de compilação do projeto para um executável.


## Considerações

Ainda trabalhando em `level2`, `level3`, `level4`, `level5`, `level6`, `level7`, `level8` e `level9`.

Atualmente o macro só foi testado na resolução 800x480, então talvez não funcione corretamente com as demais resoluções.

Apenas suportado no Idioma PT BR, futuramente irei adicionar suporte para o Inglês. 

O arquivo `level1.py`, que é responsável por automatizar as missões, ainda não está 100% completo. Na seleção de fases, não consegui incluir todas as opções. Enquanto isso, você pode ir até `data\level\level1` e trocar a imagem `m2` pela fase que deseja jogar. Recomendo o uso do Lightshot para capturar as imagens.

Exemplo:

![m2](https://github.com/user-attachments/assets/95392baf-6313-4640-bd8a-a125bf0ba589) ![m2b](https://github.com/user-attachments/assets/c02adeff-acad-41db-bda0-06ce5db8d23c) ![m2c](https://github.com/user-attachments/assets/a677a861-27c8-4d58-8e85-6d828d4b41ec)

Ainda em desenvolvimento, interface gráfica (GUI) usando a biblioteca Pygame.
 
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
2. compile o projeto em um único arquivo:
	```bash
	pyinstaller --onefile --noconsole --icon=icon.ico --add-data "data;data" main.py
	```
	
## Dicas e Soluções de Problemas

- **Problema: O macro não encontra a imagem.**
  - Certifique-se de que a imagem está na resolução correta e no formato suportado.
  - Verifique se o arquivo de imagem está no diretório correto (`data\level\level$`).
  
- **Problema: O macro trava ou não responde.**
  - Pressione a tecla 'ESC' no console para interromper o macro. 
  - Verifique se a resolução da tela está configurada para 800x480.

- **Problema: O macro não está executando as missões corretamente.**
  - Tente trocar a imagem `m2` pela fase que deseja jogar, conforme indicado na seção de considerações.

## Contribuições

![marca_small](https://github.com/user-attachments/assets/3a29afa3-0b39-43ee-9760-cca03d978e62)

-------

Sinta-se à vontade para contribuir! Abra um issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](https://github.com/rafaelitoto895/Tfregues-auto-BTH/blob/main/LICENSE.txt).










Para melhorar o README do seu repositório, aqui estão algumas sugestões:

---

# Tfregues-auto-BTH

Este é um macro para o jogo *Bit Heroes*, desenvolvido pelo usuário 'fregues', com o objetivo de otimizar o jogo ao máximo. Atualmente, o macro utiliza um método de detecção de imagens para realizar o *AFK FARM*, tornando-o ideal para automatizar tarefas repetitivas, como missões e exploração enquanto você está longe do teclado.

## Funcionalidades
- **Detecção automática de imagens**: O macro usa um sistema de reconhecimento de imagem para identificar e clicar automaticamente nos elementos da interface do jogo.
- **AFK Farming**: Configure o macro para jogar por você enquanto realiza outras atividades.
- **Reconexão automática**: Caso o servidor do jogo caia, o macro detecta e realiza o procedimento de reconexão automaticamente.
- **Controle por GUI**: O macro possui uma interface gráfica desenvolvida com Pygame, facilitando seu uso e controle.
- **Suporte ao idioma PT-BR**: O macro está totalmente em português, com previsão de suporte para inglês no futuro.

## Arquivos do Projeto

- **/data**: Contém as imagens e recursos necessários para o funcionamento do macro.
- **/logs**: Armazena registros de execução, permitindo monitoramento do desempenho.
- **level0.py**: Arquivo com funções comuns usadas pelos diferentes níveis do macro.
- **level1.py**: Lógica principal do primeiro nível do macro, responsável por automatizar as missões.
- **main.py**: Arquivo principal que inicializa a interface gráfica e o controle do macro.

Futuramente, planejamos adicionar mais níveis como `level2`, `level3`, etc.

## Requisitos

Para utilizar este projeto, você precisará instalar as seguintes dependências:

```bash
pip install opencv-python numpy pyautogui pygame
```

## Executando o Macro

1. Clone o repositório:
    ```bash
    git clone https://github.com/rafaelitoto895/Tfregues-auto-BTH.git
    ```

2. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute o macro com o seguinte comando:
    ```bash
    python main.py
    ```

## Compilando para Executável

Você pode compilar o projeto em um único executável, seguindo os passos abaixo:

1. Certifique-se de que as dependências estão instaladas:
    ```bash
    pip install opencv-python numpy pyautogui pygame pyinstaller
    ```

2. Compile o projeto:
    ```bash
    pyinstaller --onefile --noconsole --icon=icon.ico --add-data "data;data" main.py
    ```

## Atualizando Versão Automática

Ao realizar alterações, a versão do programa será automaticamente atualizada. Para compilar e mover os arquivos necessários, execute o script de automação presente no repositório.

## Contribuições

Contribuições são bem-vindas! Se você encontrou algum bug ou tem ideias para melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License.

---

Essas sugestões ajudam a organizar as informações e facilitam a compreensão para os usuários.