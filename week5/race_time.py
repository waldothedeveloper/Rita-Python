chevys = []
fords = []
result = []
Fordwin = []
Chevywin = []


car = 1
print("---Input Chevy Times---")
for x in range(8):
    ch = float(input(f"Enter time for Chevy Car {car}: "))
    chevys.append(ch)
    car += 1

car = 1
print("---Input Ford Times---")
for x in range(8):
    frd = float(input(f"Enter time for Ford Car {car}: "))
    fords.append(frd)
    car += 1

print(f"This is chevys {chevys}")
print(f"This is fords {fords}")


# Ch = [5.4, 7.2, 4.0, 9.1, 5.8, 3.9, 6.2, 8.1]
# Frd = [5.8, 6.9, 3.9, 9.2, 5.8, 3.8, 6.0, 8.5]

for i in range(8):
    if fords[i] > chevys[i]:
        result.append(f"Chevy by {round(fords[i] - chevys[i], 2)} sec")
        Chevywin.append(round(fords[i] - chevys[i], 2))
    elif fords[i] < chevys[i]:
        result.append(f"Ford by {round(chevys[i] - fords[i], 2)} sec")
        Fordwin.append(round(chevys[i] - fords[i], 2))
    elif fords[i] == chevys[i]:
        result.append("tie")

print("And the winners are:")
for i in range(8):
    print(result[i])


if len(Fordwin) > len(Chevywin):
    print("And the winning team is: F O R D !")
elif len(Fordwin) < len(Chevywin):
    print("And the winning team is: C H E V Y !")
elif len(Fordwin) == len(Chevywin):
    print("There was a tie!")
