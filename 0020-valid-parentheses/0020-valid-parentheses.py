class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        openTypes = ['(', '{', '[']
        closeTypes = [')', '}', ']']

        for c in s:
            if c in openTypes:
                stack.append(c)
                continue
            
            if c in closeTypes:
                if len(stack) == 0:
                    return False

                top = stack[-1]
                if top in closeTypes:
                    return False
                
                if top != pairs[c]:
                    return False

                stack.pop() 

        return len(stack) == 0
                