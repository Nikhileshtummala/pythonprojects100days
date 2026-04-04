def two_sum(nums, target):
    array = {}  # stores number -> index

    for i in range(len(nums)):
        match = target - nums[i]

        # Check if complement exists
        if match in array:
            return [nums[array[match]], nums[i]]

        # Store current number
        array[nums[i]] = i

    return []  # if no solution
nums = [3, 2, 5, 9, 11, -1]
target = 10

result = two_sum(nums, target)

print("values:", result)
