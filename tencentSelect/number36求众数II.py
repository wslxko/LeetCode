'''
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:

输入: [3,2,3]
输出: [3]
示例 2:

输入: [1,1,1,3,3,2,2,2]
输出: [1,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def majorityElement(self, nums):
        setNums = list(set(nums))
        result = []
        for num in setNums:
            if nums.count(num) > len(nums) / 3:
                result.append(num)
        return result


if __name__ == '__main__':
    a = Solution()
    nums = [1, 1, 1, 3, 3, 2, 2, 2]
    print(a.majorityElement(nums))
