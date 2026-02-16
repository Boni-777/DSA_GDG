class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        major=nums[0]
        freq=1
        for i in range (n):
            if nums[i]==nums[i-1]:
                freq+=1
            else:
                freq=1
            major=nums[i]
            if freq>n/2:
                return major
