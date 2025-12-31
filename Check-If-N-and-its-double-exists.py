class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                if arr[j]==2*arr[i]:
                    return True
                if arr[i]==2*arr[j]:
                    return True
        return False
