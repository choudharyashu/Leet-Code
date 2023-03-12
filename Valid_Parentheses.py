class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        top=0
        for c in s:
            if len(stack)==0:
                stack.append(c)
                top=0
            elif (stack[top]=='(' and c==')') or (stack[top]=='['and c==']') or (stack[top]=='{' and c=='}'):
                stack.pop()
                top-=1
            else:
                stack.append(c)
                top+=1
        if len(stack)==0:
            return True
        else:
            return False