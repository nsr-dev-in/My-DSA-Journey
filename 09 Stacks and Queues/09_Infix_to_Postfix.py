class Solution:
    def priority(self,ch):
        if ch=="+" or ch=="-":
            return 1
        elif ch=="*" or ch=="/":
            return 2
        elif ch=="^":
            return 3
        else:
            return 0
    
    def InfixToPostfix(self,s):
        stack=[]
        result=[]

        for char in s:
            if ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9"):
                result.append(char)

            elif char=="(": #PUSH
                stack.append(char)
            elif char==")": #POP
                while stack and stack[-1]!="(":
                    result.append(stack.pop())
                stack.pop()
            
            else:
                while stack and self.priority(stack[-1]) >= self.priority(char):
                    result.append(stack.pop())
                stack.append(char)

        while stack:
            result.append(stack.pop())

        return "".join(result)