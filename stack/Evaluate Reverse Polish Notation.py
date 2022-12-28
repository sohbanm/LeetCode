class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
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