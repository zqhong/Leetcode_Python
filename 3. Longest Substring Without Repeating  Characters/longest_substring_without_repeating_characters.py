# coding: utf8


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 最长子串长度
        answer = 0

        # 当前子串的合法左边界位置
        left = 0

        # 保存字符元素上次出现的位置
        last = {}

        for i in range(len(s)):
            # 子串中出现重复字符，变更left至上一次s[i]出现位置之后
            if s[i] in last and last[s[i]] >= left:
                left = last[s[i]] + 1
            last[s[i]] = i
            answer = max(answer, i-left+1)

        return answer

# 'dvdf
# print Solution().lengthOfLongestSubstring('dvdf')
