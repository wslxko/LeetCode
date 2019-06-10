'''
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def removeElements(List, value):
    a = List.count(value)
    for i in range(a):
        List.remove(value)
    return List


nums = [0, 1, 2, 2, 3, 0, 2, 3, 3, 4, 5, 6, 7, 2, 1, 3, 5, 6, 4, 2]
value = 2

print(removeElements(nums, value))
