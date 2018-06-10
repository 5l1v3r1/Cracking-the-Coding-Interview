# Implement the “paint  ll” function that one might see on many image editing pro- grams That is, given a screen (represented by a 2-dimensional array of Colors), a point, and a new color,  ll in the surrounding area until you hit a border of that color

def show(screen):
    for row in screen:
        print(row)
    print(5*'-')

def click(screen, x, y, color, base=None):
    if x < len(screen) and y < len(screen[0]):
        if base is None: base = screen[x][y]

        if screen[x][y] == base and screen[x][y] != color:
            screen[x][y] = color
            click(screen, x + 1, y, color, base)
            click(screen, x - 1, y, color, base)
            click(screen, x, y + 1, color, base)
            click(screen, x, y - 1, color, base)

if __name__ == '__main__':
    screen = [[1,1,1,1,1,1,1],
              [1,1,0,0,1,0,1],
              [1,0,1,1,0,0,1],
              [1,0,0,1,0,0,1],
              [1,1,1,1,1,1,1]]

    show(screen)
    click(screen, 0, 0, 5)
    show(screen)
    click(screen, 1, 5, 5)
    show(screen)
    click(screen, 2, 1, 5)
    show(screen)
    click(screen, 1, 2, 5)
    show(screen)
    click(screen, 0, 0, 0)
    show(screen)