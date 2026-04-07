class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        start = 0
        maxlength = 0
        for i in range(len(s)):
            if s[i] not in hm:
                hm[s[i]]=1
                maxlength=max(maxlength,i-start+1)
            else:
                while(s[i] in hm):
                    hm.pop(s[start])
                    start+=1
                hm[s[i]]=1
        return maxlength

                


