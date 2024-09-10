class Solution:
    def reverse(self, x: int) -> int:
        v = abs(x)
        sum =0
        while(v!=0):
            mod = v%10
            sum = (sum*10) + mod
            v = v//10
        if ((-2**31) > sum or sum >(2**31) -1):
            return 0
        return sum if x>0 else -sum