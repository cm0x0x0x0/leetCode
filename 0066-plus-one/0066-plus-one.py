class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        decimal = 0
        # convert digits to decimal
        for idx, digit in enumerate(reversed(digits)):
            decimal += pow(10, idx) * digit
            
        decimal+=1

        # convert decimal to digits
        result = [int(digit) for digit in str(decimal)]

        return result