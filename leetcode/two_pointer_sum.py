def pairSum(nums, target):
    l = 0
    r = len(nums) - 1

    while l < r:
        s = nums[l] + nums[r]

        if s == target:
            return [l, r]
        elif s < target:
            l += 1
        else:
            r -= 1

print(pairSum([1,2,3,4,6], 6))




/////////
sorted i/p requi......