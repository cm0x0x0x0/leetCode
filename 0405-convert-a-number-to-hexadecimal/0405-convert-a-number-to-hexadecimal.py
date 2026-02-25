class Solution:
    def toHex(self, num: int) -> str:
        table = {
            0: '0',
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f'
        }
        DIVISOR = 16

        result = ""
        arr = []
        
        if num == 0:
            return "0"

        num &= (2**32 - 1)

        while num > 0:
            mod = num % DIVISOR
            arr.append(mod)
            num //= 16
        
        for n in arr[::-1]:
            result += table[n]
        
        return result


        
