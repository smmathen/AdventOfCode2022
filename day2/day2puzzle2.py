score = 0

L = 0
D = 3
W = 6

R = 1
P = 2
S = 3
with open("in2.txt") as f:
    for row in f.read().strip().split("\n"):
        chars = row.split()
        opp = chars[0]
        elf = chars[1]

        # draw = 3, win = 6, lost = 0

        if opp == "A":  # they chose rock
            if elf == "X":  # need to lose
                # you choose scissors
                score += L + S
            elif elf == "Y":  # need to draw
                # you choose rock
                score += D + R
            else:
                # you choose paper
                score += W + P
        elif opp == "B":  # they chose paper
            if elf == "X":  # need to lose
                # you choose rock
                score += L + R
            elif elf == "Y":  # need to draw
                # you choose paper
                score += D + P
            else:
                # you choose scissors
                score += W + S
        elif opp == "C":  # they chose scissors
            if elf == "X":  # need to lose
                # you choose paper
                score += L + P
            elif elf == "Y":  # need to draw
                # you choose scissors
                score += D + S
            else:
                # you choose rock
                score += W + R

print("Score: " + str(score))
