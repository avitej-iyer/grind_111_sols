class Solution:
    def trap(self, height: List[int]) -> int:
        list_len = len(height)
        
        left_arr = [0]*list_len
        right_arr = [0]*list_len

        # preprocessing for left max
        for x in range(list_len):
            if x == 0 :
                left_arr[x] = height[x]
            else:
                left_arr[x] = max(left_arr[x-1], height[x])

        # preprocessing for right max
        for x in reversed(range(list_len)):
            if x == list_len-1:
                right_arr[x] = height[x]  
            else:
                right_arr[x] = max(right_arr[x+1], height[x])

        # for each height element, the most water it can hold is the 
        # MINIMUM of the left max and right max - and we need to subtract 
        # the height of the block itself from this t get the water held in that column.

        # simply return the sum of this list

        return sum([min(left_arr[x], right_arr[x])-height[x] for x in range(list_len)])       