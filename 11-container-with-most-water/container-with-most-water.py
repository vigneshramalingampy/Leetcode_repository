class Solution:
    def maxArea(self, height: List[int]) -> int:

        # result = 0
        # for x in range(len(height)):
        #     for y in range(len(height)):
        #         if x!=y:
        #             lenghter = abs(x-y)
        #             area = lenghter *min(height[x],height[y])
        #             if result < area:
        #                 result = area
        # return result
        left  =0
        right = len(height)-1
        result = 0
        while(left<right):

            lenghter = right-left
            area = lenghter * min(height[right],height[left])
            if result < area:
                result = area
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return result