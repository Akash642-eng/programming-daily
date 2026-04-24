def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

    return nums

print(rotate([1,2,3,4,5], 2))
