'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
'''


def findIndex(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif target not in nums:
            nums.append(target)
            return nums
        else:
            pass


nums = [1, 2, 3, 4, 5, 6]
num1 = 4
num2 = 7

print(findIndex(nums, num1))
print(findIndex(nums, num2))
