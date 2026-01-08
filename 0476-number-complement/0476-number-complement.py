class Solution:
    def findComplement(self, num: int) -> int:
        bitLength = num.bit_length()
        complement = ~(num ^ 0)

        return complement & ((1 << bitLength)-1)
