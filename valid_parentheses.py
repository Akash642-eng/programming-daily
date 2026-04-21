# valid parentheses

# check if brackets are valid

def isValid(s):
    stack = []
    m = {')':'(', '}':'{', ']':'['}

    for c in s:
        if c in m:
            if not stack or stack[-1] != m[c]:
                return False
            stack.pop()
        else:
            stack.append(c)

    return not stack


print(isValid("()[]{}"))  # True

# mistake:
# earlier forgot to check empty stack