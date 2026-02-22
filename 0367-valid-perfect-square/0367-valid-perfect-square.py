class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        MAX_NUM = 2**31
        squares = set()

        for n in range(MAX_NUM):
            k = n * n
            if k < 0 or k >= MAX_NUM:
                break

            squares.add(k)

        return num in squares