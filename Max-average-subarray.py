class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        CurrS=maxS=sum(nums[:k])
        for i in range(k,len(nums)):
            CurrS+=nums[i]-nums[i-k]
            maxS=max(maxS,CurrS)
        return maxS/k
