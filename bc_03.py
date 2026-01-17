import random



# def random_number_generator():
#     number = random.getrandbits(2)
#     print(number)

# random_number_generator()

# option = ("stone", "paper", "scissor")

# print(random.choice(option)) 

# cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# random.shuffle(cards)
# print(cards)

low = 1
high = 100
guesses = 0
number = random.randint(low,high)

while True:
    guess = int(input(f"Enter a number between ({low} -{high}):"))
    guesses += 1
    if guess > number:
        print("The number is too high")
    elif guess < number:
        print("The number is too low")
    else:
        print("This guess is correct")
        break
    

print(f"This round took you {guesses} guesses !! ")