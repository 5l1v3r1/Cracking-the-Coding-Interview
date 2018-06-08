# Write a method to decide if two strings are anagrams or not

from collections import Counter

# use count list
def isAnagram1(s1, s2):
    return Counter(s1) == Counter(s2)

# use sorting
def isAnagram2(s1, s2):
    return sorted(s1) == sorted(s2)

if __name__ == '__main__':
    print(isAnagram1('salam', 'lamsa'))
    print(isAnagram1('salamm', 'salam'))
    print(isAnagram2('salam', 'lamsa'))
    print(isAnagram2('salamm', 'salam'))
