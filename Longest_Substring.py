class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        result=0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[r])
            result=max(result,r-left+1)
        return result