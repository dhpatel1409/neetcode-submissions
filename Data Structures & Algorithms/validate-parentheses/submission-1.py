class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch=='(' or ch=='{' or ch=='[':
                stack.append(ch)

            else:
                if not stack:
                    return False
                poped=stack.pop()
                if (ch==')' and poped=='(') or (ch=='}' and poped=='{') or (ch==']'and poped=='['):
                    continue

                else:
                    return False

        return len(stack)==0
                    

        