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

# Variável de controle para parar o nível
should_stop = False

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
    global should_stop
    level1.run_level1()

# Loop principal
def main():
    global should_stop
    start_alpha = 0
    stop_alpha = 0
    run_alpha = 0
    credits_alpha = 0
    current_screen = "menu"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if run_button.collidepoint(pygame.mouse.get_pos()) and current_screen == "menu":
                    current_screen = "game"
                elif credits_button.collidepoint(pygame.mouse.get_pos()) and current_screen == "menu":
                    pass  # Função de créditos não implementada
                elif start_button.collidepoint(pygame.mouse.get_pos()) and current_screen == "game":
                    should_stop = False  # Reseta a variável
                    threading.Thread(target=run_level1).start()  # Inicia level1 em uma nova thread
                elif stop_button.collidepoint(pygame.mouse.get_pos()) and current_screen == "game":
                    should_stop = True  # Interrompe o processo

        screen.fill(BLACK)

        if current_screen == "menu":
            button_width, button_height = 140, 50
            run_button = pygame.Rect((WIDTH - button_width) // 2, 80, button_width, button_height)
            credits_button = pygame.Rect((WIDTH - button_width) // 2, 150, button_width, button_height)

            run_alpha = draw_button("Run", run_button, RED, run_alpha)
            credits_alpha = draw_button("Credits", credits_button, RED, credits_alpha)

        elif current_screen == "game":
            screen.fill(BLACK)  # Fundo preto
            button_width, button_height = 140, 50
            start_button = pygame.Rect((WIDTH - button_width) // 2, 80, button_width, button_height)
            stop_button = pygame.Rect((WIDTH - button_width) // 2, 150, button_width, button_height)

            start_alpha = draw_button("Start", start_button, RED, start_alpha)
            stop_alpha = draw_button("Stop", stop_button, RED, stop_alpha)

        pygame.display.flip()

if __name__ == "__main__":
    main()
