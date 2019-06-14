'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def threeSumClosest(self, nums, target):
        value_list = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    value = nums[i] + nums[j] + nums[k]
                    value_list.append(value)

        result_list = []
        for result in value_list:
            if result >= 0:
                a = result - target
                result_list.append(a)
            elif result < 0:
                a = target - result
                result_list.append(a)

        min_result = min(result_list)
        index = result_list.index(min_result)

        return value_list[index]


a = Solution()
b = [-1, 2, 1, -4]
print(a.threeSumClosest(b, 1))
