class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        L = []
        for x in range(length):
            for y in range(length):
                sum = nums[x]+nums[y]
                if(x!=y and target == sum):
                    L=[x,y]
                    break
        return L

        