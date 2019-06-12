'''
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def theNumberOf(nums):
    new_list = []
    numbers = []
    nums_set = list(set(nums))
    nums_set.sort(key=nums.index)
    for i in nums_set:
        counts = (i, nums.count(i))
        new_list.append(counts)

    all_counts = 0
    for index in range(len(new_list)):
        all_counts += new_list[index][1]

    for index in range(len(new_list)):
        if new_list[index][1] > all_counts / 2:
            numbers.append(new_list[index][0])
    return numbers


nums = [2, 2, 1, 1, 1, 2, 2]
print(theNumberOf(nums))
