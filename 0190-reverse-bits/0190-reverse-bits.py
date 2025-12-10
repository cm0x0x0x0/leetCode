class Solution:
    def reverseBits(self, n: int) -> int:
        def dec2bin(dec: int) -> str:
            result = ""
            while dec:
                temp = dec % 2
                result = str(temp) + result
                dec //= 2

            diff = 32 - len(result)
            result = "0"*diff + result

            return result
        
        def bin2dec(binStr: str) -> int:
            result = 0
            for idx,c in enumerate(binStr[::-1]):
                result += int(c) * pow(2, idx)

            return result
        
        def reverse(binStr: str) -> str:
            result = ""
            for c in binStr[::-1]:
                result += c

            return result

        originalBin = dec2bin(n)
        reverseBin = reverse(originalBin)

        return bin2dec(reverseBin)