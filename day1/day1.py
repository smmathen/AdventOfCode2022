
mostTotal = 0
total = 0
with open("input.txt") as file:
    for row in file.read().strip().split("\n"):
        if row == "":
            mostTotal = max(mostTotal, total)
            total = 0
        else:
            total += int(row)


print(mostTotal)
