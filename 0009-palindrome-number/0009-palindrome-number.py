class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = str(x)
        rev2 = "".join(reversed(rev))
        if rev2 == rev:
            return(True)
        else:
            return(False)