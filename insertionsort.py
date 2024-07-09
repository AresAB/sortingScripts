# O(n^2)
def insertion_sort(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            if i > 0: i -= 2
        i += 1
    return nums
