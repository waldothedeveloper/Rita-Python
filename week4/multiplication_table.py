while True:
  n = int(input("What size multiplication table would you like(2 - 10)"))
  if n >= 2 and n <= 10:
    break
  else:
    print("Invalid entry - Enter a number between 2 and 10")

print()
title = "--- Multiplication Table (10 x 10) ---\n"
print(title.center(50))

for row in range(1,n+1):
  for col in range(1,n+1):
    if row % 2 == 0:
      print(f"{row*col} #", end="\t")
    else:
      print(row*col, end="\t")
  print()
