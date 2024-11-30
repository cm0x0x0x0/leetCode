class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def isSameSign(num1, num2):
            if num1 < 0 and num2 < 0:
                return True
            
            if num1 > 0 and num2 > 0:
                return True
            
            return False
        
        def solution(stack, target, curIdx, length):
            while curIdx < length:
                if len(stack) == 0:
                    stack.append(target[curIdx])
                    curIdx += 1
                    continue

                top = stack[-1]
                if top > 0 and target[curIdx] < 0:
                    if abs(top) > abs(target[curIdx]):
                            curIdx += 1
                    elif abs(top) == abs(target[curIdx]):
                            stack.pop()
                            curIdx += 1        
                    else:
                        stack.pop()
                else:
                    stack.append(target[curIdx])
                    curIdx += 1

            return stack
        

        length = len(asteroids)
        stack = []
        stack.append(asteroids[0])
        return solution(stack[:], asteroids[:], 1, length)