# class Solution:
#     def minimumDistance(self, nums: List[int]) -> int:
#         hm={}
#         res=999999
#         for i in range(len(nums)):
#             if nums[i] in hm:
#                 if (len(hm[nums[i]])==3):
#                     if (hm[nums[i]][1]-hm[nums[i]][0])>(i-hm[nums[i]][2]):
#                         hm[nums[i]].pop(0)
#                 hm[nums[i]].append(i)
#             else:
#                 hm[nums[i]] =[i]
#         print(hm)
#         for k,v in hm.items():
#             if len(v) >= 3:
#                 print(v)
#                 res = min(self.calculate_score(v[0],v[1],v[2]),res)
#         if res == 999999:
#             return -1
#         return res
#     def calculate_score(self,x:int,y:int,z:int)->int:
#         return abs(x-y)+abs(y-z)+abs(z-x)
    


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        hm = {}
        res = float('inf')
        
        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]].append(i)
                
                # maintain window size 3
                if len(hm[nums[i]]) > 3:
                    hm[nums[i]].pop(0)
                
                # when we have exactly 3 → compute
                if len(hm[nums[i]]) == 3:
                    x, y, z = hm[nums[i]]
                    res = min(res, self.calculate_score(x, y, z))
            else:
                hm[nums[i]] = [i]
        
        return res if res != float('inf') else -1

    def calculate_score(self, x: int, y: int, z: int) -> int:
        return abs(x - y) + abs(y - z) + abs(z - x)