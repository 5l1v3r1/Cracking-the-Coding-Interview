def par(l, r=0):
    if r == 0 and l == 0:
        return [""]

    res = []
    if l > 0:
        res += ['(' + x for x in par(l-1, r+1)]
    if r > 0:
        res += [')' + x for x in par(l, r-1)]
    return res

if __name__ == '__main__':
    print(par(3))