class Solution:
    def isValid(self, s: str) -> bool:
        def isAPair(x, y):
            if x == '(' and y == ')':
                return True
            if x == '{' and y == '}':
                return True
            if x == '[' and y == ']':
                return True
            
        stack = []
        
        for x in s:
            if x == '(' or x == "{" or x == "[":
                stack.append(x)
            else:
                if len(stack) == 0 or not isAPair(stack.pop(), x):
                    return False
        return len(stack) == 0
