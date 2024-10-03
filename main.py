import level0
import level1
import pygame
import sys

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

# Função para desenhar um botão com efeito de transparência
def draw_button(text, rect, color, hover_color, alpha):
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

# Loop principal
def main():
    run_alpha = 0  # Opacidade inicial do botão Play
    credits_alpha = 0  # Opacidade inicial do botão Credits

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # Botões
        button_width, button_height = 140, 50
        run_button = pygame.Rect((WIDTH - button_width) // 2, 80, button_width, button_height)
        credits_button = pygame.Rect((WIDTH - button_width) // 2, 150, button_width, button_height)

        # Desenha os botões
        run_alpha = draw_button("Run", run_button, RED, GREY, run_alpha)
        credits_alpha = draw_button("Credits", credits_button, RED, GREY, credits_alpha)

        # Atualiza a tela
        pygame.display.flip()

if __name__ == "__main__":
    main()
    pass