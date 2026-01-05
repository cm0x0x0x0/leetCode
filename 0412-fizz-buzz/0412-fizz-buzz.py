class Solution:
    FIZZ_BUZZ = "FizzBuzz"
    FIZZ = "Fizz"
    BUZZ = "Buzz"

    def answer(self, n: int) -> string:
        three = n % 3 == 0
        five = n % 5 == 0

        if three and five:
            return self.FIZZ_BUZZ
        
        if three:
            return self.FIZZ
        
        if five:
            return self.BUZZ
        
        return str(n)

    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for idx in range(n):
            result.append(self.answer(idx+1))
        
        return result


            

