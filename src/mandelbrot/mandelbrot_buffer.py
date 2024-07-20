import numpy as np
import pygame
from mandelbrot import Mandelbrot

class MandelbrotBuffer:
    """
    The MandelbrotBuffer class handles the calculation and caching of the Mandelbrot set
    for a given screen resolution and zoom level. It maintains a buffer of previous calculations
    to avoid recalculating the same points repeatedly.

    Attributes:
        width (int): The width of the screen.
        height (int): The height of the screen.
        mandelbrot (Mandelbrot): An instance of the Mandelbrot class.
        zoom (float): The current zoom level.
        offset (tuple): The current offset in the complex plane.
        image (numpy.ndarray): The image buffer storing the calculated colors.
    """

    def __init__(self, width, height, max_iter):
        self.width = width
        self.height = height
        self.mandelbrot = Mandelbrot(max_iter)
        self.zoom = 1.0
        self.offset = (-0.5, 0.0)
        self.image = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.update_image()

    def update_image(self):
        """
        Update the image buffer with the current zoom and offset.
        """
        for x in range(self.width):
            for y in range(self.height):
                re = 3.5 * (x / self.width - 0.5) / self.zoom + self.offset[0]
                im = 2.0 * (y / self.height - 0.5) / self.zoom + self.offset[1]
                c = complex(re, im)
                m = self.mandelbrot.calculate(c)
                color = self.mandelbrot.color_map(m)
                self.image[y, x] = color

    def zoom_in(self, pos, factor):
        """
        Zoom in or out at a given position.

        Args:
            pos (tuple): The (x, y) position to zoom in on.
            factor (float): The zoom factor.
        """
        x, y = pos
        re = 3.5 * (x / self.width - 0.5) / self.zoom + self.offset[0]
        im = 2.0 * (y / self.height - 0.5) / self.zoom + self.offset[1]
        self.offset = (re, im)
        self.zoom *= factor
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAIT)
        self.update_image()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def center_on(self, pos):
        """
        Center the view on a given position.

        Args:
            pos (tuple): The (x, y) position to center on.
        """
        x, y = pos
        re = 3.5 * (x / self.width - 0.5) / self.zoom + self.offset[0]
        im = 2.0 * (y / self.height - 0.5) / self.zoom + self.offset[1]
        self.offset = (re, im)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAIT)
        self.update_image()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def draw(self, surface):
        """
        Draw the image buffer to the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the image on.
        """
        transposed_image = np.transpose(self.image, (1, 0, 2))
        pygame.surfarray.blit_array(surface, transposed_image)
