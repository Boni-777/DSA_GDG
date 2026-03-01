class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        i = 0
        j = 0
        current_sum = 0
        min_len = float('inf')

        while j < n:
            current_sum += nums[j]

            while current_sum >= target:
                min_len = min(min_len, j - i + 1)
                current_sum -= nums[i]
                i += 1

            j += 1

        return 0 if min_len == float('inf') else min_len
