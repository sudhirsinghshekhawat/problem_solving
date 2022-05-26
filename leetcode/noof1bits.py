class NoOf1Bits:
    def no_of_1_bits(self, n: int) -> int:
        sum = 0
        while n != 0:
            sum += 1
            n &= n - 1
        return sum


class TestNoOf1Bits:
    def setup(self):
        self.no_1_bits = NoOf1Bits()

    def test_no_of_1_bits(self):
        n = 1
        assert self.no_1_bits.no_of_1_bits(n) == 1
