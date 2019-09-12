class Solution:
    def findDiagonalOrder(self, matrix):
        if len(matrix) == 0:
            return []
        M, N, result = len(matrix), len(matrix[0]), []
        for curve_line in range(M + N - 1):
            # 起始行,curve_line从0开始
            if curve_line <= N - 1:
                row_begin = 0
            else:
                row_begin = curve_line + 1 - N
            # 结束行：最后的M条对角线的结束行均为M-1，则curve_line>=M+N-1-N=>curve_line>=M-1
            if curve_line + 1 >= M:
                row_end = M - 1
            else:
                row_end = curve_line

            if curve_line % 2 == 1:
                # range函数生成列表不包含最后需要单独处理
                # 奇数条对角线，向左下
                for i in range(row_begin, row_end + 1):
                    result.append(matrix[i][curve_line - i])
            else:
                # 偶数行对角线，向右上
                for i in range(row_end, row_begin - 1, -1):
                    result.append(matrix[i][curve_line - i])
        return result


m = Solution()
matrix = [[2, 3]]
print(m.findDiagonalOrder(matrix))
