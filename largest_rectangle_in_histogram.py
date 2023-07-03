class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_smaller = [None] * len(heights)
        right_smaller = [None] * len(heights)
        stack = []
        #fill left_smaller array 
        for idx,val in enumerate(heights):
            while stack and heights[stack[-1]] >= val:
                    stack.pop()
            if not stack:
                #no element is less than current in left side
                left_smaller[idx] = 0
            else:
                #stack[-1] is the smallest element, thats why we are adding 1
                left_smaller[idx] = stack[-1]+1
                
            stack.append(idx)

        stack = []
        #fill right_smaller array 
        for idx in range(len(heights)-1,-1,-1):
            val = heights[idx]
            while stack and heights[stack[-1]] >= val:
                stack.pop()
            if not stack:
                right_smaller[idx] = len(heights) - 1
            else:
                #stack[-1] is the smallest element and as we are traversing right to left, that's why subtracting 1
                right_smaller[idx] = stack[-1] - 1
            
            stack.append(idx)

        max_area = 0
        #for each bar we have what is the smallest in left and right
        for idx,height in enumerate(heights):
            bars = right_smaller[idx] - left_smaller[idx] + 1
            area = bars * height
            max_area = max(max_area, area)
        return max_area



