class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ls=[]
        ls.append(-1)
        ls.append(-1)
        for i in range(len(nums)-1):
            for j in range (i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    ls[0]=i
                    ls[1]=j
                    return ls
        return ls
        