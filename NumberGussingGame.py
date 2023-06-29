import random

print("***Welcome To Number Guessing Game***")
print("Game Rules!!!")
print("1. Guess the correct Number between the range of 1 - 100 ")
print("2. There will be 10 attempt for Guessing the correct number")
print("3. For wrong Guess a hind will be provided")
op=1
print("select Below Option to play the game \n 1)Play \n 2)Quit")
op=int(input())
while(op == 1 ):        
    
    user=input("Enter Your Name : ")
    num=random.randint(1 , 100)

    for i in range(11) :
        guess=int(input("Enter Your Guess:"))
        if(guess == num):
            print("Correct Guess!! You have Won !!")
            break
        else:
            if(guess > num):
                print("Your Guess Was Too High ")
            else:
                print("Your Guess was Too Low")

    if(guess != num):
        print("The Game IS Over . \n NO Attempt Left. \n The Number is " +num)

    print("Continue the game ?")
    print("select Below Option to play the game \n 1)Play \n 2)Quit")
    op=int(input())
    
print("Thank You For Playing The Game :} ")

