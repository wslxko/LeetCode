'''给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


#不是原地
def ArrayToHeavy(List):
    new_list = []
    for i in List:
        if i not in new_list:
            new_list.append(i)
    return new_list


#原地
def ArrayToHeavy1(List):
    new_List = list(set(List))
    new_List.sort(key=List.index)
    return new_List

a = ['1', '2', '4', '3', '1', '4', '2', '5', '6', '4', '5', '7', '1']

print(ArrayToHeavy(a))
print(ArrayToHeavy1(a))