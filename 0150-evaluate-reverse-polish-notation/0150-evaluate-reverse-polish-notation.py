class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(token)
                continue
            
            num2 = int(stack.pop())
            num1 = int(stack.pop())

            calc = 0
            if token == '+':
                calc = num1 + num2
            elif token == '-':
                calc = num1 - num2
            elif token == '*':
                calc = num1 * num2
            elif token == '/':
                calc = int(num1 / num2)
            
            stack.append(calc)
        
        return int(stack[-1])
