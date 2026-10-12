class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums_dummy = list(set(nums))

        for x in nums_dummy:
            if(nums.count(x) == 1):
                return(x)