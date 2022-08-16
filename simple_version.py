import random
# Get Random Number
random_num = random.randint(0,1000)
#print(random_num)
# set up
print("You have 10 tries to pick the right number between 0 and 1000. Good Luck!")

# Get user to guess random number (MAX 10 tries)
total_try = 1
while total_try < 11:
    guess = int(input("what is your guess: "))
    if guess not in range(1000):
        print("Not a valid input")
    elif guess < random_num:
        print("Your guess to small.")
        total_try += 1
    elif guess > random_num:
        print("Your guess is to large")
        total_try += 1
    else:
        break

if total_try <= 11 and guess == random_num:
    print("You have won!")
else:
    print("You lose, better luck next time.")