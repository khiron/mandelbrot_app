from .mandelbrot import Mandelbrot

class MandelbrotBuffer:
    """
    The MandelbrotBuffer class handles caching of the Mandelbrot set calculations.

    Attributes:
        cache (dict): A dictionary to store previously calculated Mandelbrot set values.
        mandelbrot (Mandelbrot): An instance of the Mandelbrot class to perform calculations.
    """

    def __init__(self, max_iter):
        self.cache = {}
        self.mandelbrot = Mandelbrot(max_iter)

    def get_value(self, c):
        """
        Get the Mandelbrot set value for a given complex number c. If the value is cached, return it.
        Otherwise, calculate it, cache it, and then return it.

        Args:
            c (complex): The complex number to check.

        Returns:
            int: The number of iterations before the function diverges or max_iter if it doesn't.
        """
        if c in self.cache:
            return self.cache[c]
        else:
            value = self.mandelbrot.calculate(c)
            self.cache[c] = value
            return value
