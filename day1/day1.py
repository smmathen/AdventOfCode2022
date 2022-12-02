
mostTotal = 0
total = 0
all_sums = []
with open("input.txt") as file:
    for row in file.read().strip().split("\n"):
        if row == "":
            # mostTotal = max(mostTotal, total)
            all_sums .append(total)
            total = 0
        else:
            total += int(row)

in_order = sorted(all_sums, reverse=True)
print(sum(in_order[:3]))
