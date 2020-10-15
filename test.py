def seak(nums, target, k):
    if k == 0 or not nums:
        if target == 0:
            return 1
        else:
            return 0
    result = []
    for i,v in enumerate(nums):
        result.append(seak([l for j,l in enumerate(nums) if j != i], target - v, k - 1))
    return 1 if sum(result) != 0 else 0
print(seak([2,8,-5,6,-10,3,7],0,3))
print(seak([2,3,1,22,5],0, 3))