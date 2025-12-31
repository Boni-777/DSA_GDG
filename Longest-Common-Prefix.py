class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref= strs[0]
        ans= ""
        for i in range(len(pref)):
            for s in strs[1:]:
                if i== len(s) or s[i]!=pref[i]:
                    return ans
            ans+= pref[i]
        return ans

 
