'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

2=abc,3=def,4=ghi,5=jkl,6=mno,7=pqrs,8=tuv,9=wxyz

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def letterCombinations(label, digits):
    n = len(digits)
    if len(digits) == 0:
        return []
    elif len(digits) == 1:
        return label[digits]
    count = 1
    x = label[digits[0]]
    y = label[digits[count]]
    while count < n:
        record = []
        for i in x:
            for j in y:
                record.append(i + j)
        count += 1
        x = record[:]
        if count < n:
            y = label[digits[count]]
    return x


dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'qprs', '8': 'tuv', '9': 'wxyz'}
num = '23'
# print(input(num, dict))
print(letterCombinations(dict, '234'))
