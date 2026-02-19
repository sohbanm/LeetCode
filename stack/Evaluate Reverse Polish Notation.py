# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

# first attempt
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        symbols = {"+","-","*","/"}
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in symbols:
                stack.append(int(tokens[i]))

            else:
                if tokens[i] == "+":
                    one = stack.pop()
                    two = stack.pop()
                    stack.append(two + one)

                elif tokens[i] == "-":
                    one = stack.pop()
                    two = stack.pop()
                    stack.append(two - one)

                elif tokens[i] == "*":
                    one = stack.pop()
                    two = stack.pop()
                    stack.append(two * one)

                else:
                    one = stack.pop()
                    two = stack.pop()
                    stack.append(int(two / one)) #number always rounds down

        return stack[0]
    
# second attempt, cleaner
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens:
            if t.isnumeric() or (t[0] == '-' and t[1:].isnumeric()):
                stack.append(int(t))
            else:
                first, second = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(first + second)
                elif t == "-":
                    stack.append(second - first)
                elif t == "*":
                    stack.append(first * second)
                elif t == "/":
                    stack.append(int(second / first))

        return stack[-1]