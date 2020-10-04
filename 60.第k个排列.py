#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
# class Solution:
#     def getPermutation(self, n: int, k: int) -> str:
#         def backtrack(index, candidate):
#             if index == n:
#                 return [[]]
#             result = []
#             for i in candidate:
#                 result += [[str(i)] + x for x in backtrack(index + 1, 
#                 [x for x in candidate if x != i])]
#             return result
#         return "".join(backtrack(0, list(range(1,n+1)))[k - 1])
# class Solution:
#     def getPermutation(self, n: int, k: int) -> str:
#         def factorial(n):
#             result = 1
#             for i in range(1,n):
#                 result *= i
#             return result
        
#         def backtrack(candidate, k):
#             if not candidate:
#                 return candidate
#             each_num = factorial(len(candidate))
#             next_value = candidate[k // each_num - 1]
#             return [next_value] + backtrack([x for x in candidate if x != next_value],
#             k - each_num * (k // each_num - 1) )
#         return backtrack(list(range(1, n+1)), k)

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)
        
        k -= 1
        ans = list()
        valid = [1] * (n + 1)
        for i in range(1, n + 1):
            order = k // factorial[n - i] + 1
            for j in range(1, n + 1):
                order -= valid[j]
                if order == 0:
                    ans.append(str(j))
                    valid[j] = 0
                    break
            k %= factorial[n - i]

        return "".join(ans)

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/permutation-sequence/solution/di-kge-pai-lie-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
            


# @lc code=end

a = Solution()
print(a.getPermutation(3,3))