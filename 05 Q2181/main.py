#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 22:59
# @Author  : Ly
# @File    : main.py
# @Software: PyCharm
# @Github  : https://github.com/ly8073


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_ListNode(nums):
    node = None
    for val in nums[-1:0:-1]:
        before_node = ListNode(val, node)
        node = before_node
    head = ListNode(nums[0], node)
    return head


def list_to_ListNode_skip(nums):
    node = None
    for val in nums[-1:0:-1]:
        if val == 0:
            continue
        before_node = ListNode(val, node)
        node = before_node
    head = ListNode(nums[0], node)
    return head


class Solution:
    def mergeNodes(self, head: [ListNode]) -> [ListNode]:
        res = []
        node = head.next
        tmp = 0
        while node is not None:
            if node.val == 0:
                res.append(tmp)
                tmp = 0
            tmp += node.val
            node = node.next
        return list_to_ListNode_skip(res)




if __name__=="__main__":
    test_list_node = list_to_ListNode([0,3,1,0,4,5,2,0])
    res = Solution().mergeNodes(test_list_node)
    print("done")
