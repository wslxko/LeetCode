'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def noRepeatingString(string):
    all_list = []
    repeat_list = []
    str_list = list(string)
    for first_str in range(len(str_list)):
        for second_str in range(first_str + 1, len(str_list)):
            value = str_list[first_str:second_str]
            value_str = ''.join(value)
            all_list.append(value_str)

    for num in all_list:
        set_num = list(set(num))
        for i in set_num:
            if num.count(i) > 1:
                repeat_list.append(num)

    for repeat_num in range(len(repeat_list)):
        all_list.remove(repeat_list[repeat_num])

    all_list.sort(reverse=True)

    return len(all_list[0])


a = "abcabcbb"
b = "bbbbb"
c = "pwwkew"
# print(noRepeatingString(a))
print(noRepeatingString(b))
print(noRepeatingString(c))
