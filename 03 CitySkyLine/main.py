#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 13:24
# @Author  : Ly
# @File    : main.py
# @Software: PyCharm
# @Github  : https://github.com/ly8073
from typing import List


class Solution:
    def find_max(self, grid: List[List[int]]):
        rowMax = list(map(max, grid))
        colMax = list(map(max, zip(*grid)))
        return rowMax, colMax

    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        """
        ans[i, j] = min(max(grid[:, j]), max(grid[i,:]))其实就是找到所在行列中最大值的最较小值
        :param grid:
        :return:
        """
        total = 0
        row_max, col_max = self.find_max(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                total += (min(row_max[i], col_max[j]) - grid[i][j])
        return total


if __name__=="__main__":
    print(Solution().maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))