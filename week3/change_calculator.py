import sys

print("################################################")
print("#                                              #")
print("#            CHANGE CALCULATOR                 #")
print("#                                              #")
print("################################################\n")

coin_denominations = [25,10,5,1]
coin_counts = []

def change_calculator():
  cents = int(input("Please enter the number of cents(0-99): "))

  for d in coin_denominations:
    coin_counts.append(cents//d)
    cents = cents % d

def result():
    print(" ")
    print("Quarters:", coin_counts[0])
    print("Dimes:", coin_counts[1])
    print("Nickels:", coin_counts[2])
    print("Pennies:", coin_counts[3])


while True:
  change_calculator()
  result()
  print(" ")
  cont = input("Continue? (y/n): ")
  if cont.strip().lower() != "y":
    print("Bye!")
    break
sys.exit()