import random

mynumber = random.randint(1,10)
print("Welcome to my Guess the number program!")
print(f"This is the guess number just for testing purposes: {mynumber}")

def guessNumber():
    count = 1
    while True:
        try:
          while True:
            guess = int(input("Guess a number between 1 and 10: "))

            if guess < mynumber:
              print("Too low")
              count += 1
            elif guess > mynumber:
              print("Too high")
              count += 1
            elif guess == mynumber:
              print(f"You guessed it! It took you {count} attempts")
              break
          break
        except ValueError:
              print(f"Please enter a number, letters are NOT allowed")
              count += 1

if __name__ == "__main__":
  guessNumber()