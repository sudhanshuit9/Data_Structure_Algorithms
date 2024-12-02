#Given an array representing heights, calculate how much rainwater can be trapped.
def trap_rain_water(heights):
    stack = []
    water_trapped = 0

    for i, h in enumerate(heights):
        while stack and h > heights[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            bounded_height = min(h, heights[stack[-1]]) - heights[top]
            water_trapped += distance * bounded_height
        stack.append(i)

    return water_trapped

# Example Usage
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap_rain_water(heights))  # Output: 6
