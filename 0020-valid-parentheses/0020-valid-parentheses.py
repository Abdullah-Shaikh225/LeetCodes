class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {")" : "(", "]" : "[", "}" : "{"}
        stack = []
        for i in s:
            if i in dict:
                if stack and dict[i] == stack[-1]:  
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)    
        return not stack    