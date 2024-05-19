import random


# get_next_guess checks if the number that has been put in by the user is a valid one 
def get_next_guess():
    number = int(input(""))
    while number < 1111 or number > 9999:
        print("Invalid input! Please try again:")
        number = int(input(""))
    return(number)


# split_digits splits up the digits into individual items of a list
def split_digits(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    return digits[::-1]


# compare_numbers compares the two numbers to find the correct number of black and white markers
def compare_numbers(random_number, user_input):
    numberOfDigitsRN = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    for i in range(4):
        numberOfDigitsRN[random_number[i]]+=1 
        
    numberOfDigitsUI = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    for i in range(4):
        numberOfDigitsUI[user_input[i]]+=1 
        
    numberOfWhiteMarkers = 0
    for i in range(10):
        numberOfWhiteMarkers += min(numberOfDigitsRN[i], numberOfDigitsUI[i])  

    numberOfBlackMarkers = 0 
    for i in range (4):
        if random_number[i] == user_input[i]:
            numberOfBlackMarkers += 1

    numberOfWhiteMarkers_final =  numberOfWhiteMarkers - numberOfBlackMarkers 
    return(numberOfWhiteMarkers_final + numberOfBlackMarkers*10) 


random_number = []
for i in range(4): 
    random_number.append(random.randint(1,9))
secret_number = int("".join(map(str, random_number))) 


# this marks the actual beginning of the game
print("Welcome to Mastermind! Let's find out if you are one!")
print("Before you enter your first guess, please note that your number can only consist of 4 digits and cannot contain any zeros.")
print("Now, please enter your first guess: ")
guess = get_next_guess()
counter = 1
user_input = split_digits(guess)


if secret_number == guess:
    print("Congratulations, you guessed it! And on your first guess too! That's very impressive!")
    print("You definitely are a Mastermind!")
    
while random_number != user_input:
    if counter == 10:
        print("You did not guess the number correctly :(")
        print("The right answer was", secret_number)
        print("Better luck next time!")
        quit()
        
    results = compare_numbers(random_number, user_input)
    print("Number of correctly placed digits:", results//10) 
    print("Number of digits that are in the number, but not in their correct place yet:", results%10) 
    counter += 1
    print("----- Try #", counter, "-----")
    print("Enter your next guess: ")
    guess = get_next_guess()
    user_input = split_digits(guess)            
        
print("Congratulations, you guessed it! You must be a true Mastermind!")
