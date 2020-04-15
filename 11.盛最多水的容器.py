#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
# class Solution:
#     def track(self, left, right):
#         if right - left == 1:
#             return min(self.height[right], self.height[left])

#         if self.dp[left][right - 1] != None:
#             case1 = self.dp[left][right - 1]
#         else:
#             case1 = self.track(left, right - 1)

#         if self.dp[left + 1][right] != None:
#             case2 = self.dp[left + 1][right]
#         else:
#             case2 = self.track(left + 1, right)

#         result = max(case1,
#                  case2,
#                  min(self.height[left], self.height[right]) * (right - left))
#         self.dp[left][right] = result 

#         return result

#     def maxArea(self, height) -> int:
#         self.height = height
#         self.dp = [[None for y in range(len(height))] 
#         for x in range(len(height))]

#         return self.track(0, len(height) - 1)


#     height = None
#     dp = None

class Solution:
    def maxArea(self, height) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/container-with-most-water/solution/container-with-most-water-shuang-zhi-zhen-fa-yi-do/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

a = Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))
