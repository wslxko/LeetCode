'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

示例1：
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

示例2：
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
'''


def combinationOfArray(nums):
    new_list = []
    for i in nums:
        new_list.append(str(i))
    input = int(''.join(new_list))
    output = str(input + 1)
    result = list(output)
    return result


nums = [1, 2, 3, 4]
nums1 = [2, 4, 7, 9]
print(combinationOfArray(nums))
print(combinationOfArray(nums1))
