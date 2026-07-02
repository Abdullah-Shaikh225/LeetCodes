class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ds = ""
        for i in range(len(min(strs,key=len))):
            for j in range (len(strs)):
                if strs[j][i] == strs[0][i]:
                    pass
                else:
                    return(ds)
            ds += strs[0][i]
        return(ds)