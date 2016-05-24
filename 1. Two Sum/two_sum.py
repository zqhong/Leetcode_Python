# coding: utf8


class Solution(object):
    def twoSum(self, nums, target):
        """
        大致思路：
        1. 将 nums 列表转换为字典，字典取出元素的空间复杂度为：O(1)。
        2. 遍历 nums 列表，计算出期待值：target-num1。查找字典是否有该期望值

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_key = [i for i in range(len(nums))]
        nums_dict = dict(zip(nums, nums_key))

        for k, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in nums_dict:
                index = nums_dict[num2]
                if index != k:
                    return [k, index]
        raise ValueError('No two sum solution')
