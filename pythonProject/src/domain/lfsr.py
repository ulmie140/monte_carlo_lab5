class LFSRGenerator:
    """
    Генератор псевдослучайных чисел на основе 32-битного полинома
    Полином: X^32+X^31+X^30+X^29+X^27+X^26+X^25+X^24+X^23+X^21+X^20+X^17+X^16+X^14+X^12+X^9+X^8+X^7+1
    """

    def __init__(self, seed: int = 0xACE1ACE1):
        self.state = seed
        self.taps = [31, 30, 29, 28, 26, 25, 24, 23, 22, 20, 19, 16, 15, 13, 11, 8, 7, 6]

    def step(self) -> float:
        """Сдвиг регистра и возврат числа в диапазоне [0, 1)."""
        feedback = 0
        for tap in self.taps:
            feedback ^= (self.state >> tap) & 1

        self.state = ((self.state << 1) & 0xFFFFFFFF) | feedback
        return self.state / 0xFFFFFFFF