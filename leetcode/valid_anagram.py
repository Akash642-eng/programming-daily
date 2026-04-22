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

/////////////////////////////////////////


from collections import Counter
import time
import random
import string

s = ''.join(random.choices(string.ascii_lowercase, k=1000000))
t = ''.join(random.choices(string.ascii_lowercase, k=1000000))

start = time.time()
print(Counter(s) == Counter(t))
print(f"Counter: {(time.time()-start)*1000:.2f}ms")             // check runtime for Counter

start = time.time()
print(sorted(s) == sorted(t))
print(f"Sorted: {(time.time()-start)*1000:.2f}ms")              // check runtime for sorted
