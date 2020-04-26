#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i != len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i = i + 1
        return len(nums)
# @lc code=end

