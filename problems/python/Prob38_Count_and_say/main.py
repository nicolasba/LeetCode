def binarySearch(nums, target, start, end):

    mid = (start + end) // 2

    if nums[mid] == target:
        return mid
    
    if end <= start:
        return -1

    if nums[mid] < target:
        return binarySearch(nums, target, mid + 1, end)
    else:
        return binarySearch(nums, target, start, mid)
    

l = [1, 0]
print(binarySearch(l, 1, 0, len(l)))