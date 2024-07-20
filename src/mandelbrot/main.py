import pygame
from typing import Tuple
from .mandelbrot_view import MandelbrotView

# Constants
WIDTH: int = 800
HEIGHT: int = 600
MAX_ITER: int = 100
ZOOM_FACTOR: float = 2.0
BUTTON_COLOR: Tuple[int, int, int] = (50, 50, 50)
TEXT_COLOR: Tuple[int, int, int] = (255, 255, 255)
BUTTON_PADDING: int = 10

def draw_buttons(screen: pygame.Surface) -> Tuple[pygame.Rect, pygame.Rect]:
    """
    Draws the zoom in and zoom out buttons on the screen.

    Args:
        screen (pygame.Surface): The surface to draw the buttons on.

    Returns:
        tuple: Rectangles defining the area of the zoom in and zoom out buttons.
    """
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

def main() -> None:
    """
    Main function to run the Mandelbrot Set visualization using Pygame.
    This function initializes Pygame, sets up the display, and enters the main loop
    where it handles events, updates the display, and maintains the frame rate.
    """
    # Initialize Pygame
    pygame.init()
    
    # Set up the display
    screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Mandelbrot Set')
    
    # Create a clock object to manage the frame rate
    clock: pygame.time.Clock = pygame.time.Clock()
    
    # Create an instance of the MandelbrotView class
    mandelbrot_view: MandelbrotView = MandelbrotView(WIDTH, HEIGHT, MAX_ITER)
    
    # Main loop
    running: bool = True
    while running:
        # Fill the screen with a black background
        screen.fill((0, 0, 0))
        
        # Draw the Mandelbrot set and buttons on the screen
        mandelbrot_view.draw(screen)
        zoom_in_rect, zoom_out_rect = draw_buttons(screen)
        
        # Update the display
        pygame.display.flip()
        
        # Get the current mouse position
        mouse_pos: Tuple[int, int] = pygame.mouse.get_pos()
        
        # Change the cursor based on its position
        if zoom_in_rect.collidepoint(mouse_pos) or zoom_out_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if zoom_in_rect.collidepoint(event.pos):
                    mandelbrot_view.zoom_in((WIDTH // 2, HEIGHT // 2), ZOOM_FACTOR)
                elif zoom_out_rect.collidepoint(event.pos):
                    mandelbrot_view.zoom_in((WIDTH // 2, HEIGHT // 2), 1 / ZOOM_FACTOR)
                elif event.button == 1:  # Left mouse button
                    mandelbrot_view.center_on(event.pos)

        # Maintain the frame rate at 30 frames per second
        clock.tick(30)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
