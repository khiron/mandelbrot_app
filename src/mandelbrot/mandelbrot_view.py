import numpy as np
import pygame
from typing import Tuple
from .mandelbrot_buffer import MandelbrotBuffer

class MandelbrotView:
    """
    The MandelbrotView class handles the visualization of the Mandelbrot set.

    Attributes:
        width (int): The width of the screen.
        height (int): The height of the screen.
        mandelbrot_buffer (MandelbrotBuffer): An instance of the MandelbrotBuffer class.
        zoom (float): The current zoom level.
        offset (Tuple[float, float]): The current offset in the complex plane.
        image (np.ndarray): The image buffer storing the calculated colors.
    """

    def __init__(self, width: int, height: int, max_iter: int):
        self.width: int = width
        self.height: int = height
        self.mandelbrot_buffer: MandelbrotBuffer = MandelbrotBuffer(max_iter)
        self.zoom: float = 1.0
        self.offset: Tuple[float, float] = (-0.5, 0.0)
        self.image: np.ndarray = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.update_image()

    def update_image(self) -> None:
        """
        Update the image buffer with the current zoom and offset.
        """
        for x in range(self.width):
            for y in range(self.height):
                real: float = 3.5 * (x / self.width - 0.5) / self.zoom + self.offset[0]
                imaginary: float = 2.0 * (y / self.height - 0.5) / self.zoom + self.offset[1]
                complex_number: complex = complex(real, imaginary)
                iterations: int = self.mandelbrot_buffer.get_value(complex_number)
                color: Tuple[int, int, int] = self.mandelbrot_buffer.mandelbrot.color_map(iterations)
                self.image[y, x] = color

    def zoom_in(self, pos: Tuple[int, int], factor: float) -> None:
        """
        Zoom in or out at a given position.

        Args:
            pos (Tuple[int, int]): The (x, y) position to zoom in on.
            factor (float): The zoom factor.
        """
        x, y = pos
        real: float = 3.5 * (x / self.width - 0.5) / self.zoom + self.offset[0]
        imaginary: float = 2.0 * (y / self.height - 0.5) / self.zoom + self.offset[1]
        self.offset = (real, imaginary)
        self.zoom *= factor
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAIT)
        self.update_image()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def center_on(self, pos: Tuple[int, int]) -> None:
        """
        Center the view on a given position.

        Args:
            pos (Tuple[int, int]): The (x, y) position to center on.
        """
        x, y = pos
        real: float = 3.5 * (x / self.width - 0.5) / self.zoom + self.offset[0]
        imaginary: float = 2.0 * (y / self.height - 0.5) / self.zoom + self.offset[1]
        self.offset = (real, imaginary)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAIT)
        self.update_image()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the image buffer to the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the image on.
        """
        transposed_image: np.ndarray = np.transpose(self.image, (1, 0, 2))
        pygame.surfarray.blit_array(surface, transposed_image)
