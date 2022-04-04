#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 1:52
# @Author  : Ly
# @File    : main.py
# @Software: PyCharm
# @Github  : https://github.com/ly8073


class Solution:
    def minimumSum(self, num: int) -> int:
        """
        题目描述了是四位数，此方法可适用于多位数
        :param num:
        :return:
        """
        nums = sorted(map(int, str(num)), reverse=True)
        ans, power = 0, 0
        for i in range(0, len(nums), 2):
            if i + 1 < len(nums):
                ans += ((nums[i] + nums[i + 1]) * (10 ** power))
            else:
                ans += (nums[i] * (10 ** power))
            power += 1
        return ans


if __name__=="__main__":
    print(Solution().minimumSum(129320))