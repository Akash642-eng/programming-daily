# contains duplicate

def containsDuplicate(nums):
    seen = set()

    for n in nums:
        if n in seen:
            return True
        seen.add(n)

    return False


print(containsDuplicate([1,2,3,1]))  # True


..................

one, 
was slow