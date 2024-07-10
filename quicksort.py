# O(nlog(n))
# complexity changes wildly depending on what pivots are given, from O(log(n)) to O(n^2) if the list is already sorted
def quick_sort(nums, low, high):
    if low < high:
        i = partition(nums, low, high)
        sorted = quick_sort(nums, low, i - 1)
        sorted.append(nums[i])
        sorted.extend(quick_sort(nums, i + 1, high))
        return sorted
    return nums[low:]

def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i
