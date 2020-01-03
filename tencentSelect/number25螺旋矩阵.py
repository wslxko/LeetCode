'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def spiralOrder(self, matrix):
        outList = []
        for indexOuter in range(len(matrix)):
            for indexInner in range(len(matrix[indexOuter])):
                if indexOuter == 0:
                    outList.append(matrix[indexOuter][indexInner])
                if indexOuter != 0 and indexOuter != len(matrix) - 1 and indexInner == 0:
                    outList.append(matrix[indexOuter][len(matrix[indexOuter]) - 1])
                if indexOuter == len(matrix) - 1:
                    outList.append(matrix[indexOuter][-indexInner - 1])
        for indexOuter in range(len(matrix)):
            for indexInner in range(len(matrix[indexOuter])):
                if indexOuter != 0 and indexOuter != len(matrix) - 1 and indexInner != len(matrix[indexOuter]) - 1:
                    outList.append(matrix[indexOuter][indexInner])
        return outList


if __name__ == "__main__":
    a = Solution()
    outList = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(a.spiralOrder(outList))
