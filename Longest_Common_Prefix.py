class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=""
        strs=sorted(strs)
        for i in range(0,len(strs[0])):
            if (strs[0][i]!=strs[-1][i]):
                return res
            res+=strs[0][i]
        return res