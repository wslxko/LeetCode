'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例：
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

'''


def sumAny(nums):
    max_sub_sum = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sub_sum = 0
            for k in range(i, j):
                sub_sum += nums[k]
                if sub_sum > max_sub_sum:
                    max_sub_sum = sub_sum
    return max_sub_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(sumAny(nums))
