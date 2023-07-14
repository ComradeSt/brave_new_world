def start_screen():
    print("-----WELCOME-----")
    print("-------to--------")
    print("------TIC--------")
    print("------TAC--------")
    print("------TOE--------")
    print("                 ")
    print("                 ")

def show():
    print()
    print("     0   1   2   ")
    for i, row in enumerate(field):
        row_str = f"  {i}  {'  '.join(row)}  "
        print(row_str)
    print()

def ask():
    while True:
        cords = input("  Enter coordinates: ").split()
        
        if len(cords) != 2:
            print(" ENTER 2 COORDINATES ")
            continue
        
        x, y = cords
        
        if not(x.isdigit()) or not(y.isdigit()):
            print(" DIGITS ONLY ")
            continue
        
        x, y = int(x), int(y)
        
        if 0 > x or x > 2 or  0 > y or  y > 2 :
            print(" OUT OF RANGE ")
            continue
        
        if field[x][y] != " ":
            print(" CELL TAKEN ¯\_(ツ)_/¯ ")
            continue
        
        return x, y
            
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("X WINS!")
            return True
        if symbols == ["0", "0", "0"]:
            print("0 WINS!")
            return True
    return False

start_screen()
field = [[" "] * 3 for i in range(3) ]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" X move")
    else:
        print(" 0 move")
    
    x, y = ask()
    
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    
    if check_win():
        break
    
    if count == 9:
        print(" DRAW ")
        break