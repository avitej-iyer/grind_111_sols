class Solution:
    def maxArea(self, height: List[int]) -> int:

        # two pointer approach - start from the ends and move the pointer with the smaller height
        # towards the other pointer
        left_point, right_point = 0, len(height) - 1
        max_vol = 0

        while left_point < right_point:
            # at each iteration, we calculate the volume of the container formed by the two pointers
            # and update the max volume if necessary
            min_height = min(height[left_point], height[right_point])
            max_vol = max(max_vol, min_height*abs(left_point-right_point))
            if height[left_point] < height[right_point]:
                left_point += 1
                # we can save some time by skipping over the heights that are smaller than the current min_height
                while height[left_point] < min_height:
                    left_point += 1

            else:
                right_point -= 1
                while height[right_point] < min_height:
                    right_point -= 1

        return max_vol                 