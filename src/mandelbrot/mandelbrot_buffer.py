from typing import Dict, Tuple
from .mandelbrot import Mandelbrot

class MandelbrotBuffer:
    """
    The MandelbrotBuffer class handles caching of the Mandelbrot set calculations and tracks cache hits and misses.

    Attributes:
        cache (Dict[complex, int]): A dictionary to store previously calculated Mandelbrot set values.
        mandelbrot (Mandelbrot): An instance of the Mandelbrot class to perform calculations.
        hits (int): The number of cache hits.
        misses (int): The number of cache misses.
    """

    def __init__(self, max_iter: int):
        self.cache: Dict[complex, int] = {}
        self.mandelbrot: Mandelbrot = Mandelbrot(max_iter)
        self.hits: int = 0
        self.misses: int = 0

    def get_value(self, c: complex) -> int:
        """
        Get the Mandelbrot set value for a given complex number c. If the value is cached, return it.
        Otherwise, calculate it, cache it, and then return it.

        Args:
            c (complex): The complex number to check.

        Returns:
            int: The number of iterations before the function diverges or max_iter if it doesn't.
        """
        if c in self.cache:
            self.hits += 1
            return self.cache[c]
        else:
            self.misses += 1
            value: int = self.mandelbrot.calculate(c)
            self.cache[c] = value
            return value

    def get_cache_stats(self) -> Tuple[int, int]:
        """
        Get the cache hit and miss statistics.

        Returns:
            Tuple[int, int]: A tuple containing the number of hits and misses.
        """
        return self.hits, self.misses
