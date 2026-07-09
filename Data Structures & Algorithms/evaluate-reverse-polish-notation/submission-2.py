class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in "+-/*":
                stack.append(i)
            else:
                right=int(stack.pop())
                left=int(stack.pop())
                operator=i
                if i == "+":
                    stack.append(right + left)
                elif i == "-":
                    stack.append(left-right)
                elif i == "/":
                    stack.append(left/right)
                elif i == "*":
                    stack.append(right*left)
        
        return int(stack[0])