from turtle import right


print('Welcome to Treasure Island')
choice1 = input('Your are choice? "left" or "right": ').lower().strip()

if choice1 == "left":
    #continue
    choice2 = input('Your are choice? "swim" or "wait": ').lower().strip()
    if choice2 == "swim":
        #continue
        choice3 = input('Your are choice? "yellow" or "red" or "blue": ').lower().strip()
        if choice3 == "yellow":
            print("You Win@@")
        elif choice3 == "red":
            print("you choice = red . Game Over !!!")
        elif choice3 == "blue":
            print("you choice = blue . Game Over !!!")
        else:
            print("Game Over !!!")    
    else:
        print("Game Over !!!")
else:
    print("Game Over !!!")



