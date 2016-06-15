# coding: utf8


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        大致思路：
        计算需要用到的索引值，合并两个已排序的数组。当找到需要的值的时候，退出合并。

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        nums_len_sum = nums1_len + nums2_len

        # nums1 和 nums2 均为空
        if nums_len_sum == 0:
            return 0

        nums_len_average = nums_len_sum / 2

        # 计算需要用到的索引值
        need_indexs = []
        # 偶数
        if nums_len_sum % 2 == 0:
             need_indexs.extend([nums_len_average-1, nums_len_average])
        # 奇数
        else:
            need_indexs.append(nums_len_average)

        # nums1、nums2 中有一个为空
        if nums1_len == 0 or nums2_len == 0:
            current_nums = nums1 if nums1_len != 0 else nums2
            return sum([current_nums[i] for i in need_indexs])/float(len(need_indexs))

        # nums1 和 nums2 均不为空
        # 合并 nums1 和 nums2，当找到需要的值的时候，停止合并
        new_nums = []
        left = 0
        right = 0
        for i in range(max(need_indexs)+1):
            # 超过索引范围
            if left + 1 > nums1_len:
                new_nums.extend(nums2[right:])
                break
            elif right + 1 > nums2_len:
                new_nums.extend(nums1[left:])
                break
            # 找到了需要的值了
            if len(new_nums) >= max(need_indexs)+1:
                break
            if nums1[left] < nums2[right]:
                new_nums.append(nums1[left])
                left += 1
            elif nums1[left] == nums2[right]:
                new_nums.append(nums1[left])
                new_nums.append(nums2[right])
                left += 1
                right += 1
            else:
                new_nums.append(nums2[right])
                right += 1

        return sum([new_nums[i] for i in need_indexs])/float(len(need_indexs))


# 1, 2, 3, 4
# print Solution().findMedianSortedArrays([1, 4], [2, 3])