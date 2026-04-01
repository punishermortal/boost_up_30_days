class Solution:
    def hashing_with_rabin_karp(self , x : int , y : int ,z : int):
        x*=100000
        x+=y
        x*=100000
        x+=z
        return x
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        hm_set=set()
        res=[]
        for i in range(len(nums)):
            target = 0 - nums[i]
            left = i+1 # not starting from 0 if we strat from 0 then duplicate will be come
            right = len(nums) - 1
            while(left < right):
                if (nums[left] + nums[right]) > target:
                    right -=1
                elif (nums[left] + nums[right]) < target:
                    left +=1
                else:
                    val = self.hashing_with_rabin_karp(nums[i],nums[left],nums[right])
                    if  val not in hm_set:
                        res.append([nums[i],nums[left],nums[right]])
                        hm_set.add(val)
                    left += 1
                    right -= 1
        return res
        