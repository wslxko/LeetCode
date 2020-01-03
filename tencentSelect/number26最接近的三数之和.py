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
        allResult = []
        for index in range(len(nums)):
            copyNums = nums.copy()
            total = 0
            copyNums.pop(index)
            for num in copyNums:
                total += num
            allResult.append(total)

        end = []
        for index in range(len(allResult)):
            r = allResult[index] - target
            end.append(abs(r))
        indexEnd = end.index(min(end))
        return allResult[indexEnd]


if __name__ == "__main__":
    a = Solution()
    nums = [-1, 2, 1, -4]
    print(a.threeSumClosest(nums, 3))
