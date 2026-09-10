class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        b = nums1 + nums2
        b = sorted(b)
        print(b)
        lenth = len(b)
        if lenth%2 == 0:
            return (b[(lenth//2)-1] + b[(lenth//2)])/2
        else:
            return b[(lenth//2)]
        # return 0.0


        