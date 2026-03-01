class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set = {}       
        left = 0           
        max_len = 0
        for right in range(len(s)):
            if s[right] in set and set[s[right]] >= left:
                left = set[s[right]] + 1
            set[s[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len
        
