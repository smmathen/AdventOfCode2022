score = 0
with open("in2.txt") as f:
    for row in f.read().strip().split("\n"):
        chars = row.split()
        opp = chars[0]
        elf = chars[1]

        # draw = 3, win = 6, lost = 0

        if opp == "A":  # they chose rock
            if elf == "X":
                score += 4  # draw + rock
            elif elf == "Y":
                score += 8  # win + paper
            else:
                score += 3  # lost + scissors

        elif opp == "B":  # they chose paper
            if elf == "X":
                score += 1  # lost + rock
            elif elf == "Y":
                score += 5  # draw + paper
            else:
                score += 9  # win + scissors

        elif opp == "C":  # they chose scissors
            if elf == "X":
                score += 7  # win + rock
            elif elf == "Y":
                score += 2  # lose + paper
            else:
                score += 6  # draw + scissors


print("Score: " + str(score))
