class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        element=0
        for num in nums:
            element=element^num
        return element
