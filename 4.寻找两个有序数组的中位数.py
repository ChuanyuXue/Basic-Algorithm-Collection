#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start

def merge(a, b):
    i, j = 0, 0
    lenth = len(a), len(b)
    result = []
    while(i < lenth[0] or j < lenth[1]):
        if i < lenth[0] and (j >= lenth[1] or a[i] < b[j]):
            result.append(a[i])
            i += 1
        if j < lenth[1] and (i >= lenth[0] or a[i] >= b[j]):
            result.append(b[j])
            j += 1
    return result

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if len(nums1) == 0 or len(nums2) == 0:
            result = nums1 + nums2
        else:
            if nums1[0] > nums1[-1]:
                nums1 = nums1[::-1]
            if nums2[0] > nums2[-1]:
                nums2 = nums2[::-1]
            result = merge(nums1, nums2)
        
        lenth = len(result)
        if lenth % 2 == 0:
            return (result[lenth // 2 - 1] + result[lenth // 2]) / 2
        else:
            return result[lenth // 2]
        
# @lc code=end


a = Solution()
a.findMedianSortedArrays([1,2], [3,4])
