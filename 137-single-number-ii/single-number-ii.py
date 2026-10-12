class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums_dummy = list(set(nums))
        for num in nums_dummy:
            if nums.count(num) ==1:
                return num
        