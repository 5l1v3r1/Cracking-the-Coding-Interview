def isRotation(s1, s2):
    return len(s1) == len(s2) and s2 in s1+s1

if __name__ == '__main__':
    print(isRotation('salamaleyk', 'leyksalama'))
    print(isRotation('salamalek', 'leyksalamax'))
    print(isRotation('aa', 'a'))