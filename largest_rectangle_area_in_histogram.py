def largest_rectangle_area_in_histogram(heights):
    heights = [-1]+heights+[-1]
    stack = [0]
    from_left = [0]*len(heights)
    max_area = 0
    for i in range(1, len(heights)-1):
        while heights[stack[-1]] >= heights[i]:
            stack.pop()
        from_left[i] = stack[-1]
        stack.append(i)
    from_right = [0] * len(heights)
    stack = [len(heights)-1]
    for i in range(len(heights)-2, 0, -1):
        while heights[stack[-1]] >= heights[i]:
            stack.pop()
        from_right[i] = stack[-1]
        stack.append(i)
    for i in range(1,len(heights)-1):
        max_area = max(max_area, heights[i] * (from_right[i]-from_left[i]-1))
    return max_area

print(largest_rectangle_area_in_histogram([3,2,4,5,7,6,1]))