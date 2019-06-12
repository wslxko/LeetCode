'''给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


def sumTwo(List, target):
    targetList = []
    for i in range(len(List)):
        for j in range(i, len(List)):
            if List[i] + List[j] == target:
                value = List.index(List[i]), List.index(List[j])
                targetList.append(value)

    return targetList


a = [4, 10, 4, 43, 37, 20, 27]
print(sumTwo(a, 47))



