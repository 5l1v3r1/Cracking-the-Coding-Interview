HMAP = {
    0b0000: '0',
    0b0001: '1',
    0b0010: '2',
    0b0011: '3',
    0b0100: '4',
    0b0101: '5',
    0b0110: '6',
    0b0111: '7',
    0b1000: '8',
    0b1001: '9',
    0b1010: 'a',
    0b1011: 'b',
    0b1100: 'c',
    0b1101: 'd',
    0b1110: 'e',
    0b1111: 'f',

    '0': 0b0000,
    '1': 0b0001,
    '2': 0b0010,
    '3': 0b0011,
    '4': 0b0100,
    '5': 0b0101,
    '6': 0b0110,
    '7': 0b0111,
    '8': 0b1000,
    '9': 0b1001,
    'a': 0b1010,
    'b': 0b1011,
    'c': 0b1100,
    'd': 0b1101,
    'e': 0b1110,
    'f': 0b1111,

}

def toHex(num):
    global HMAP
    if num == 0: return '0x0'
    return toHex(num >> 4) + HMAP[num & 0b1111]

def toDec(num):
    global HMAP
    if num == '0x0': return 0;
    return (toDec(num[:-1]) << 4) + HMAP[num[-1:]]

if __name__ == '__main__':
    print(toHex(100))
    print(toDec('0x064'))

    print(toDec(toHex(10101010101)))
