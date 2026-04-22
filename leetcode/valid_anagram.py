def isAnagram(s, t):
    return sorted(s) == sorted(t)

print(isAnagram("anagram", "nagaram"))

..........
O(n log n)
.............................

from collection import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)

print(isAnagram("anagram", "nagaram"))
..........
o(n) - bit fast for big strings...
