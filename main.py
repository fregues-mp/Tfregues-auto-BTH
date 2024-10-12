# _,-,_,-,_,-,_,-,_,-,_,-,_ GUI||MAIN _,-,_,-,_,-,_,-,_,-,_,-,_ #
import level0
import level1
import pygame
import sys
import threading

pygame.init()

# cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (38, 38, 38)
RED = (255, 0, 0)

WIDTH, HEIGHT = 420, 280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tfregues Macro_BTH")

icone = pygame.image.load('icon.png')
pygame.display.set_icon(icone)

font = pygame.font.Font(None, 36)
version_font = pygame.font.Font(None, 18)

should_stop = False
macro_running = False

# Versão
program_version = "Versão 1.6.25"

def draw_button(text, rect, color, alpha):
    mouse = pygame.mouse.get_pos()
    is_hover = rect.collidepoint(mouse)

    if is_hover:
        alpha = min(255, alpha + 3)
    else:
        alpha = max(0, alpha - 5)

    button_surface = pygame.Surface(rect.size, pygame.SRCALPHA)
    button_surface.fill((color[0], color[1], color[2], alpha))

    screen.blit(button_surface, rect.topleft)

    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

    return alpha

def run_level1():
    global macro_running
    macro_running = True
    level1.run_level1()
    macro_running = False

# Loop principal
def main():
    global should_stop, macro_running
    start_alpha = 0
    stop_alpha = 0
    credits_alpha = 0
    current_screen = "menu"

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
                elif start_button.collidepoint(mouse_pos) and current_screen == "game" and not macro_running:
                    should_stop = False
                    threading.Thread(target=run_level1).start()
                elif stop_button.collidepoint(mouse_pos) and current_screen == "game" and macro_running:
                    level0.stop_macro()
                    while not macro_running:
                        level0.log('Macro parado com sucesso.')

        screen.fill(BLACK)

        if current_screen == "menu":
            start_alpha = draw_button("Run", run_button, RED, start_alpha)
            credits_alpha = draw_button("Credits", credits_button, RED, credits_alpha)

        elif current_screen == "game":
            screen.fill(BLACK)
            if not macro_running:
                start_alpha = draw_button("Start", start_button, RED, start_alpha)
            stop_alpha = draw_button("Stop", stop_button, RED, stop_alpha)

        version_surface = version_font.render(program_version, True, WHITE)
        version_rect = version_surface.get_rect(bottomright=(WIDTH - 10, HEIGHT - 10))
        screen.blit(version_surface, version_rect)

        pygame.display.flip()

if __name__ == "__main__":
    main()
