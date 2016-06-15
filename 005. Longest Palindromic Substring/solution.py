# coding: utf8


class Solution(object):
    def longestPalindrome(self, s):
        """
        大致思路：
        枚举回文串的对称中心位置，向两侧扫描检测最长回文长度时间复杂度为O(N^2)

        :type s: str
        :rtype: str
        """
        ansl, ansr, maxx = 0, 1, 0
        length = len(s)
        for i in range(1, length * 2):
            if i & 1 :
                left = i / 2
                right = left
            else :
                left = i / 2 - 1
                right = left + 1
            while (left >= 0) and (right < length) and (s[left] == s[right]):
                left -= 1
                right += 1
            left += 1
            right -= 1
            if right - left > maxx:
                maxx = right - left
                ansl = left
                ansr = right
        return s[ansl: ansr + 1]

# ababa
print Solution().longestPalindrome('dababaf')
