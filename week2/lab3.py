print("################################################")
print("#                                              #")
print("#            EXAM GRADE CALCULATOR             #")
print("#                                              #")
print("################################################\n")

grade = int(input("Please enter your grade:\n"))
if grade >= 90 and grade <= 100:
    print("You earned an A")
elif grade >= 80 and grade <= 89:
    print("You earned an B")
elif grade >= 70 and grade <= 79:
    print("You earned an C")
elif grade >= 60 and grade <= 69:
    print("You earned an D")
elif grade <= 59:
    print("You earned an F")
