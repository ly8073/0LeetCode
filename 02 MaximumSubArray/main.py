#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 0:10
# @Author  : Ly
# @File    : main.py
# @Software: PyCharm
# @Github  : https://github.com/ly8073

from typing import List


class Solution:
    def maxSubArray_v0(self, nums: List[int]) -> int:
        """
        ans[i]表示连续累加到第i位时的子数组和，当ans[i]小于0时，子数组可以从头开始计数了。
        :param nums:
        :return:
        """
        ans = [0] * len(nums)
        ans[0] = nums[0]
        for i, num in enumerate(nums):
            if i == 0:
                continue
            if ans[i - 1] < 0:
                ans[i] = num
            else:
                ans[i] = num + ans[i - 1]
        return sorted(ans)[-1]

    def maxSubArray_v1(self, nums: List[int]) -> int:
        """
        优化空间，在原数组上进行修改
        :param nums:
        :return:
        """
        for i in range(1, len(nums)):
            if nums[i - 1] < 0:
                continue
            else:
                nums[i] += nums[i-1]
        return sorted(nums)[-1]


if __name__=="__main__":
    solution = Solution()
    max_sub_array = solution.maxSubArray_v1([5,4,-1,7,8])
    print(max_sub_array)