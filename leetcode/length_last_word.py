def lengthOfLastWord(s):
    words = s.strip().split()
    return len(words[-1])

print(lengthOfLastWord("Hello World"))  # 5


//////
strip() → spaces caused issues

...............................
alt


def lengthOfLastWord(s):
    count = 0
    i = len(s) - 1

    while i >= 0 and s[i] == " ":
        i -= 1

    while i >= 0 and s[i] != " ":
        count += 1
        i -= 1

    return count