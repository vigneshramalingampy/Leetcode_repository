class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val)
        lem = len(nums)
        nums[:] = [x for x in nums if x !=val]
        return (lem-count)