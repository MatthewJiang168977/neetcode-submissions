class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = "+-*/" 
        for elem in tokens: 
            if elem not in op: 
                stack.append(int(elem))
            else:
                # print(stack) 
                last_elem = int(stack.pop())
                second_last = int(stack.pop())
                # print(stack)
                # print(elem)
                if elem == "+":
                    stack.append(second_last + last_elem)
                elif elem == "-":
                    stack.append(second_last - last_elem)
                elif elem == "*":
                    stack.append(second_last * last_elem)
                elif elem == "/": 
                    output = int(float(second_last) / last_elem)
                    stack.append(output)
        return stack[0]