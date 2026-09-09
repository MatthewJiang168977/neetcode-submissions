class Solution:
    def isValid(self, s: str) -> bool:
        # # seen = []
        # closed = False
        # for i in s: 
        #     for j in range(i+1, len(s)): 
        #         if s[j] == i: 
        #             closed = True
        #             # seen.append(i)
        #     closed = False

        stack = [] 
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for par in s: 
            if par in closeToOpen: 
                if stack and stack[-1] == closeToOpen[par]: 
                    stack.pop() 
                else: 
                    return False
            else: 
                stack.append(par) 
        return True if not stack else False

        