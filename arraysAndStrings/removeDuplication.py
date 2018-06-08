# Design an algorithm and write code to remove the duplicate characters in a string without using any additional bu er
from collections import OrderedDict

# use hit list
def removeDup1(s):
    hit = [False for i in range(256)]
    result = ''
    for char in s:
        if hit[ord(char)] == False:
            hit[ord(char)] = True
            result += char
    return result

# use hashTable
def removeDup2(s):
    return ''.join(set(s))

# use orderedDict
def removeDup3(s):
    return ''.join(list(OrderedDict.fromkeys(s)))

if __name__ == '__main__':
    print(removeDup1('salam khobi azizam?'))
    print(removeDup2('salam khobi azizam?'))
    print(removeDup3('salam khobi azizam?'))
