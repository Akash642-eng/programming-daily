# two sum

# problem:
# given nums and target, find 2 indices

# my thinking:
# brute force is easy but O(n^2)
# better use hashmap

def two_sum(nums, target):
    lookup = {}
    for i, n in enumerate(nums):
        if target - n in lookup:
            return [lookup[target - n], i]
        lookup[n] = i


# test
print(two_sum([2,7,11,15], 9))  # [0,1]


# mistake:
# initially forgot to store index properly
# also confused about lookup[target - n]