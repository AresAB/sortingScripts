def bubble_sort(nums):
    swapped = False
    for i in range(0, len(nums) - 1):
        if nums[i] > nums[i + 1]:
            (nums[i], nums[i + 1]) = (nums[i + 1], nums[i])
            swapped = True
    if swapped: return bubble_sort(nums)
    return nums
