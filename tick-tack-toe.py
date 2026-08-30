spaces = [1,2,3,4,5,6,7,8,9]
win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,5,8),(2,5,6)]
playing_game = True
def printboard(nums):
    print(f"""
  {nums[0]}  |  {nums[1]}  |  {nums[2]}
  ---|-----|----
  {nums[3]}  |  {nums[4]}  |  {nums[5]}
  ---|-----|----
  {nums[6]}  |  {nums[7]}  |  {nums[8]}
""")
def check_draw(spaces):
    spaces_left = 9
    for i in spaces:
        if i == 'X' or i=='O':
            spaces_left -=1
    if spaces_left == 0:
        return True
    else:
        return False
def check_win(spots,player,wins):
    for i in wins:
        if spots[i[0]]==player and spots[i[1]]==player and spots[i[2]]==player:
            return True
def computer_moves(spaces,wins):
    moved = False
    for combos in wins:
        num = 0
        spot_1 = False
        spot_2 = False
        spot_3 = False
        if spaces[combos[0]]=='X':
            spot_1 = True
            num+=1
        if spaces[combos[1]]=='X':
            spot_2 = True
            num+=1
        if spaces[combos[2]]=='X':
            spot_3 = True
            num+=1
        if num ==2:
            break
printboard(spaces)
while playing_game==True:
    player_move = int(input("What number spot would you like to take(1-9): "))
    while (player_move>9 or player_move<1):
        player_move = int(input(("Please enter a number 1-9: ")))
    spaces[player_move-1]='X'
    printboard(spaces)
    if check_draw(spaces)==True:
        print("Its a tie.")
        break
    if check_win(spaces,'X',win)==True:
        print("You win.")
        break
    if check_win(spaces,'O',win)==True:
        print("You lose.")
        break