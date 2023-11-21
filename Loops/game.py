# Design a game between user and computer as follows:
#  There are 51 balls in a basket.
#  The user has to pick less than 5 balls from the basket at a time.
#  Each user will be given his/her turn alternately.
#  The user who picks the last ball will lose the game.
#  The first turn is of the user.
#  The computer shall always win

balls=51
u=0
c=0
while balls>1:
    user=int(input("You Choose: "))
    if user<5:
        u=u+1
        computer=5-user
        c=c+1
        print(f'Computer Choose: {computer}')
        balls=balls-5
    else:
        print("Please choose less than five balls")
else:
    if u==c:
        print("Computer Won")
    else:
        print("You Won")