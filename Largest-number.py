class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max=nums[0]
        maxindex=0
        for i in range (1,len(nums)):
            if nums[i]>max:
                max=nums[i]
                maxindex=i
        for x in nums:
            if x!=max and max<2*x:
                return -1
        return maxindex
