class Solution:
    def addDigits(self, num: int) -> int:
            p = str(num)
            summ=0
            for value in p:
                digit=int(value)
                summ+=digit
            while summ>=10:
                s=str(summ)
                new_summ=0
                for values in s:
                    digitt=int(values)
                    new_summ+=digitt
                summ=new_summ
            return summ
            if num==0:
                return 0
