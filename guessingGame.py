import random
chances = 1
number = random.randint(1,9)
while chances<=5:
    guess = input("Enter your guess: ")
    if int(guess)<round(number):
        print("Your guess is less than the number. You have used",chances,"chances.")
        chances+=1
    elif int(guess)> round(number):
        print("Your guess is more than the number. You have used",chances,"chances.")
        chances+=1
    elif int(guess) == round(number):
        print("YOU WIN!")
        break
    elif chances == 5:
        print("Sorry, you lose! The correct number was",round(number))
        break