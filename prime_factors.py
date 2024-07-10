class PrimeFactor:
    def of(self, number, divisor=2) -> list[int]:
        factors = []
        if number <= 1:
            return factors

        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor

        factors += self.of(number, divisor + 1)
        return factors
