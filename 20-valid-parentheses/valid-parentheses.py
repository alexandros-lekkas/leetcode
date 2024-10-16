class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if c == "[" or c == "(" or c == "{":
                stack.append(c)
            if c == "]" or c == ")" or c == "}":
                if len(stack) == 0:
                    return False
                else:
                    peek = stack[-1]
                    if c == "]" and peek == "[":
                        stack.pop()
                    elif c == ")" and peek == "(":
                        stack.pop()
                    elif c == "}" and peek == "{":
                        stack.pop()
                    else:
                        return False

        if len(stack) != 0:
            return False
        
        return True
    