class Solution:
    def isValid(self, s: str) -> bool:
        parantheses_stack = []
        for parantheses in s:
            if parantheses in "[{(":
                parantheses_stack.append(parantheses)
            elif parantheses_stack:
                if parantheses == ")":
                    if parantheses_stack.pop() != '(':
                        return False
                elif parantheses == "]":
                    if parantheses_stack.pop() != '[':
                        return False
                elif parantheses == "}":
                    if parantheses_stack.pop() != '{':
                        return False
            else:
                return False
        return parantheses_stack==[]
            
            