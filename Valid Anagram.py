class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dilo= defaultdict(int) 
        for i in s:
            dilo[i]= dilo[i]+1
        lilo= defaultdict(int)
        for i in t:
            lilo[i]= lilo[i]+1
        if dilo==lilo:
            return True
        else:
            return False
        
 
