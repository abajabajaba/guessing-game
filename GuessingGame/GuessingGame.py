import random
print("Number guessing game")
number=random.randint(1,9)
chances=0
print("guess a number( between 1-9 )")

while chances < 5:
    guess=int(input("Enter your secret number"))

    if guess==number:
        print ("EXCELLANT YOU WON!!!")
        break    

    elif guess < number:
        print("your guess was too low")
    else:
        print("your guess was too high")
    chances +=1

if not chances < 5:
    print("You LOSE the game and the number is",number)    
