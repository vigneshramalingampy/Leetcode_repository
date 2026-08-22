class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lister = list(set(nums))
        nums[:] = sorted(lister)
        print(lister)
        return len(lister)