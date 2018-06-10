# Write a method that returns all subsets of a set

def subs(l):
    if l == []:
        return [[]]

    x = subs(l[1:])

    return x + [[l[0]] + i for i in x]

if __name__ == '__main__':
    print(subs([1, 2, 3]))