# O(nlog(n))
def merge_sort(nums):
    if len(nums) < 2: return nums
    mid = len(nums) // 2
    return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))

def merge(first, second):
    final_arr = []
    i_f = 0
    i_s = 0
    while i_f < len(first) and i_s < len(second):
        if first[i_f] <= second[i_s]:
            final_arr.append(first[i_f])
            i_f += 1
            continue
        final_arr.append(second[i_s])
        i_s += 1
    final_arr.extend(first[i_f:])
    final_arr.extend(second[i_s:])
    return final_arr
