import pygame
from .mandelbrot_buffer import MandelbrotBuffer

# Constants
WIDTH, HEIGHT = 800, 600
MAX_ITER = 100
ZOOM_FACTOR = 2
BUTTON_COLOR = (50, 50, 50)
TEXT_COLOR = (255, 255, 255)
BUTTON_PADDING = 10

def draw_buttons(screen):
    font = pygame.font.Font(None, 36)
    zoom_in_text = font.render('Zoom In', True, TEXT_COLOR)
    zoom_out_text = font.render('Zoom Out', True, TEXT_COLOR)
    
    zoom_in_rect = zoom_in_text.get_rect(topleft=(10 + BUTTON_PADDING, 10 + BUTTON_PADDING))
    zoom_out_rect = zoom_out_text.get_rect(topleft=(10 + BUTTON_PADDING, 60 + BUTTON_PADDING))
    
    # Draw button backgrounds
    pygame.draw.rect(screen, BUTTON_COLOR, (10, 10, zoom_in_text.get_width() + 2 * BUTTON_PADDING, zoom_in_text.get_height() + 2 * BUTTON_PADDING))
    pygame.draw.rect(screen, BUTTON_COLOR, (10, 60, zoom_out_text.get_width() + 2 * BUTTON_PADDING, zoom_out_text.get_height() + 2 * BUTTON_PADDING))
    
    # Draw button text
    screen.blit(zoom_in_text, zoom_in_rect)
    screen.blit(zoom_out_text, zoom_out_rect)
    
    return zoom_in_rect, zoom_out_rect

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Mandelbrot Set')
    clock = pygame.time.Clock()
    
    mandelbrot_buffer = MandelbrotBuffer(WIDTH, HEIGHT, MAX_ITER)
    running = True

    while running:
        screen.fill((0, 0, 0))
        mandelbrot_buffer.draw(screen)
        zoom_in_rect, zoom_out_rect = draw_buttons(screen)
        pygame.display.flip()
        
        mouse_pos = pygame.mouse.get_pos()
        if zoom_in_rect.collidepoint(mouse_pos) or zoom_out_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if zoom_in_rect.collidepoint(event.pos):
                    mandelbrot_buffer.zoom_in((WIDTH // 2, HEIGHT // 2), ZOOM_FACTOR)
                elif zoom_out_rect.collidepoint(event.pos):
                    mandelbrot_buffer.zoom_in((WIDTH // 2, HEIGHT // 2), 1 / ZOOM_FACTOR)
                elif event.button == 1:  # Left mouse button
                    mandelbrot_buffer.center_on(event.pos)

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
