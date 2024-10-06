# _,-,_,-,_,-,_,-,_,-,_,-,_ GUI||MAIN _,-,_,-,_,-,_,-,_,-,_,-,_ #
import level0
import level1
import pygame
import sys
import threading

# Inicializa o Pygame
pygame.init()

# Definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (38, 38, 38)
RED = (255, 0, 0)

# Configurações da tela
WIDTH, HEIGHT = 420, 280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tfregues Macro_BTH")

# Fonte para os textos
font = pygame.font.Font(None, 36)
version_font = pygame.font.Font(None, 18)  # Fonte menor para a versão

# Variáveis de controle
should_stop = False
macro_running = False  # Indica se o macro está em execução

# Versão do programa
program_version = "Versão 1.0.0"

# Função para desenhar um botão com efeito de transparência
def draw_button(text, rect, color, alpha):
    mouse = pygame.mouse.get_pos()
    is_hover = rect.collidepoint(mouse)

    # Atualiza a opacidade do botão
    if is_hover:
        alpha = min(255, alpha + 5)  # Aumenta a opacidade
    else:
        alpha = max(0, alpha - 5)     # Diminui a opacidade

    # Cria uma superfície para o botão com o fundo transparente
    button_surface = pygame.Surface(rect.size, pygame.SRCALPHA)
    button_surface.fill((color[0], color[1], color[2], alpha))  # Adiciona a opacidade

    # Desenha o botão na tela
    screen.blit(button_surface, rect.topleft)

    # Texto do botão
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

    return alpha

# Função para iniciar o level1
def run_level1():
    global macro_running
    macro_running = True
    level1.run_level1()
    macro_running = False  # Define como False quando o macro terminar

# Função para mostrar a tela de atualizações
def show_updates():
    screen.fill(BLACK)  # Limpa a tela
    updates_text = font.render("Tela de Atualizações", True, WHITE)
    updates_rect = updates_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
    screen.blit(updates_text, updates_rect)

    # Desenha o botão "Exit" no canto inferior direito
    exit_button = pygame.Rect(WIDTH - 140, HEIGHT - 50, 140, 50)
    exit_alpha = draw_button("Exit", exit_button, RED, 0)  # Botão Exit

    # Aguarda até que a tela seja fechada
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(pygame.mouse.get_pos()):  # Verifica se o botão Exit foi clicado
                    waiting = False

        pygame.display.flip()

# Loop principal
def main():
    global should_stop, macro_running
    start_alpha = 0
    stop_alpha = 0
    run_alpha = 0
    credits_alpha = 0
    current_screen = "menu"

    # Inicializa os botões
    button_width, button_height = 140, 50
    run_button = pygame.Rect((WIDTH - button_width) // 2, 80, button_width, button_height)
    credits_button = pygame.Rect((WIDTH - button_width) // 2, 150, button_width, button_height)
    start_button = pygame.Rect((WIDTH - button_width) // 2, 80, button_width, button_height)
    stop_button = pygame.Rect((WIDTH - button_width) // 2, 150, button_width, button_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if run_button.collidepoint(mouse_pos) and current_screen == "menu":
                    current_screen = "game"
                elif credits_button.collidepoint(mouse_pos) and current_screen == "menu":
                    pass  # Função de créditos não implementada
                elif start_button.collidepoint(mouse_pos) and current_screen == "game" and not macro_running:
                    should_stop = False  # Reseta a variável
                    threading.Thread(target=run_level1).start()  # Inicia level1 em uma nova thread
                elif stop_button.collidepoint(mouse_pos) and current_screen == "game" and macro_running:
                    level0.stop_macro()  # Para o macro
                    level0.log('Macro parado com sucesso.')
                elif version_rect.collidepoint(mouse_pos):  # Verifica se a versão foi clicada
                    current_screen = "updates"  # Muda para a tela de atualizações

        screen.fill(BLACK)

        if current_screen == "menu":
            run_alpha = draw_button("Run", run_button, RED, run_alpha)
            credits_alpha = draw_button("Credits", credits_button, RED, credits_alpha)

        elif current_screen == "game":
            screen.fill(BLACK)  # Fundo preto

            # Desativa o botão Start se o macro já estiver rodando
            if not macro_running:
                start_alpha = draw_button("Start", start_button, RED, start_alpha)
            stop_alpha = draw_button("Stop", stop_button, RED, stop_alpha)

        # Desenha a versão do programa no canto inferior direito
        version_surface = version_font.render(program_version, True, WHITE)  # Usa a fonte menor
        version_rect = version_surface.get_rect(bottomright=(WIDTH - 10, HEIGHT - 10))
        screen.blit(version_surface, version_rect)

        # Exibe a tela de atualizações se necessário
        if current_screen == "updates":
            show_updates()
            current_screen = "menu"  # Retorna ao menu após mostrar as atualizações

        pygame.display.flip()

if __name__ == "__main__":
    main()
