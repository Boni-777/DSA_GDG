class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p=str(n)
        productt=1
        summ=0
        for values in p:
            digit = int(values) 
            productt *= digit
            summ += digit
            diff = productt-summ
        return diff
        
