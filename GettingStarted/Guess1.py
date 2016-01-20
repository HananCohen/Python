import random

print('Hello, What\'s your favorit number')
number = input()

print('your favorit number is ' + number)


minNumber = 1
maxNumber = 1000
magicNumber = random.randint(minNumber, maxNumber)

message = "The magic number is between {0} and {1}"
print(message.format(minNumber, maxNumber))

found = False

while not found:
    print("Guess what it is")
    guess = int(input())

    if guess == magicNumber:
        found = True
        print("***")

    if guess < magicNumber:
        print("Too low")

    if guess > magicNumber:
        print("Too high")
        
print("you got it")
