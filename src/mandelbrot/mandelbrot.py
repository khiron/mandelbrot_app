import numpy as np
import pygame

class Mandelbrot:
    """
    The Mandelbrot class handles the calculation of whether a given point in the complex plane
    belongs to the Mandelbrot set. The Mandelbrot set is a set of complex numbers for which
    the function f_c(z) = z^2 + c does not diverge when iterated from z = 0.

    The complex plane is a way to represent complex numbers graphically. The x-axis represents
    the real part of the complex number, and the y-axis represents the imaginary part.

    The Mandelbrot set is fascinating because it produces a complex fractal structure from a
    seemingly simple function. As you zoom into the Mandelbrot set, you see an infinite amount
    of detail, and the boundary of the set exhibits self-similarity, where smaller parts resemble
    the whole structure.

    Attributes:
        max_iter (int): The maximum number of iterations to determine if a point is in the set.
    """

    def __init__(self, max_iter):
        self.max_iter = max_iter

    def calculate(self, c):
        """
        Calculate the number of iterations for a given complex number c to determine if it
        belongs to the Mandelbrot set.

        Args:
            c (complex): The complex number to check.

        Returns:
            int: The number of iterations before the function diverges or max_iter if it doesn't.
        """
        z = 0
        n = 0
        while abs(z) <= 2 and n < self.max_iter:
            z = z*z + c
            n += 1
        return n

    def color_map(self, n):
        """
        Map the number of iterations to a color.

        Args:
            n (int): The number of iterations.

        Returns:
            tuple: A tuple representing an RGB color.
        """
        if n == self.max_iter:
            return (0, 0, 0)  # Inside the Mandelbrot set
        else:
            return (255 - n % 256, 255 - (n * 5) % 256, 255 - (n * 15) % 256)  # Color gradient
