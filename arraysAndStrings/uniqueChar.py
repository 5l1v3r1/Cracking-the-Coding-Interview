# Implement an algorithm to determine if a string has all unique characters What if you can not use additional data structures?

# use count list
def isAllCharUnique2(s):
    checkList = [False for i in range(256)]
    for char in s:
        if checkList[ord(char) - ord('a')] == False:
            checkList[ord(char) - ord('a')] = True
        else:
            return False
    return True

# use sorting
def isAllCharUnique1(s):
    sortedS = sorted(s)

    lastChar = None
    for char in sortedS:
        if char == lastChar:
            return False
        lastChar = char
    return True

if __name__ == '__main__':
    print(isAllCharUnique1('sfsdfds'))
    print(isAllCharUnique1('salam'))
    print(isAllCharUnique1('anfgr'))
    print(isAllCharUnique2('sfsdfds'))
    print(isAllCharUnique2('salam'))
    print(isAllCharUnique2('anfgr'))
