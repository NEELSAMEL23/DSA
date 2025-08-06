
def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate the area with the current pair of lines
        width = right - left
        area = min(height[left], height[right]) * width
        max_area = max(max_area, area)
        
        # Move the pointer pointing to the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

arr = [1,8,6,2,5,4,8,3,7]
res = maxArea(arr)
print(res)
