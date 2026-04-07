# class Solution:#abba
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s)==0:
#             return 0
#         if len(s)==1:
#             return 1
#         longest_substring = 0
#         curr_string = ""
#         hm={}
#         for i in range(len(s)):
#             if s[i] in hm:
#                 if hm[s[i]]>hm[curr_string[0]]:
#                     curr_string=s[hm[s[i]]+1:i+1]
#                 hm[s[i]]=i
#             else:
#                 hm[s[i]]=i
#                 curr_string+=s[i]
#             # print(curr_string)
#             longest_substring =max(longest_substring,len(curr_string))
#         # for i in range(len(s)):
#         #     if s[i] in hm:
#         #         longest_substring = max(longest_substring , len(curr_string))
#         #         curr_string = s[i]
#         #         hm.clear()
#         #         hm[s[i]] = i
#         #     else:
#         #         hm[s[i]] = i
#         #         curr_string += s[i]
#         #     longest_substring = max(longest_substring , len(curr_string))
#         return longest_substring

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

                


