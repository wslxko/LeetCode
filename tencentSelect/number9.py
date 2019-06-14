'''
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def canPartition(self, nums):
        output = [[]]
        set_output = []
        for i in range(len(nums)):
            for j in range(len(output)):
                output.append(output[j] + [nums[i]])

        for i in output:
            if i not in set_output:
                set_output.append(i)

        p = 1
        while p < len(set_output):
            result = []
            for i in range(len(set_output)):
                i_sum = 0
                for i_num in set_output[i]:
                    i_sum += i_num
                result.append(i_sum)

            for j in range(p, len(set_output)):
                j_sum = 0
                for j_num in set_output[j]:
                    j_sum += j_num

                if j_sum in result:
                    return True
                else:
                    return False
            p += 1


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    a = Solution()
    print(a.canPartition(nums))
