from typing import List

def twoSumQuadratic(nums: List[int], target: int) -> List[int]:
    for i in range (len(nums)):
        num1 = nums[i]
        for j in range (i + 1, len(nums)):
            num2 = nums[j]

            if target == num2 + num1:
                return [i, j]


def binarySearch(nums: List[int], key: int, begin: int, end: int) -> int:
    middle_index = int((end + begin) / 2)

    if end <= begin:
        return -1

    if nums[middle_index] == key:
        return middle_index
    elif nums[middle_index] < key:
        return binarySearch(nums, key, middle_index + 1, end)
    else:
        return binarySearch(nums, key, begin, middle_index)


def twoSumNLogN(nums: List[int], target: int) -> List[int]:

    li = []
    for i in range(len(nums)):
        li.append([nums[i], i])
    li.sort()
    sorted_nums = [li[i][0] for i in range(len(li))]

    for i in range(len(sorted_nums) - 1):

        num1 = sorted_nums[i]
        j = binarySearch(sorted_nums, target - num1, i + 1, len(sorted_nums))

        if j != -1:
            unsorted_i = li[i][1]
            unsorted_j = li[j][1]
            return [unsorted_i, unsorted_j]


if __name__ == '__main__':

    print(twoSumNLogN([3,2,4], 6))
