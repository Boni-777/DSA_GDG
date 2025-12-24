class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        small_multiple= n*2
        if n%2==0:
          return n
        else:
          return small_multiple
