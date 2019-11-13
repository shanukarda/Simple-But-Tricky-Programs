total_try = 10
i = 0
while i < total_try :
    b = int(input("Guess the number:\n"))
    if b>16:
        print("You are guessing bigger number than right number.")
    elif b<16:
        print("You are guessing smaller number than right number.")
    elif b==16:
        print("Great! You guess right number.")
        break
    else:
        print("Invalid Input.")
    total_try-=1
    if b!=16:
        print("You have",total_try,"more try left:")
if b!=16:
    print("Game Over!")