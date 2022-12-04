# PART ONE

# count = 0
# with open("input.txt") as f:
#     for line in f:
#         pair = line.split(",")
#         # also getting rid of new line character below
#         first, second = pair[0], pair[1][:-1]

#         firstBreak = first.find("-")
#         secondBreak = second.find("-")

#         a1 = int(first[:firstBreak])
#         a2 = int(first[firstBreak+1:])

#         b1 = int(second[:secondBreak])
#         b2 = int(second[secondBreak+1:])

#         if a1 <= b1 and a2 >= b2 or b1 <= a1 and b2 >= a2:
#             count += 1

# print(count)


# PART TWO
count = 0
with open("input.txt") as f:
    for line in f:
        pair = line.split(",")
        # also getting rid of new line character below
        first, second = pair[0], pair[1][:-1]

        firstBreak = first.find("-")
        secondBreak = second.find("-")

        a1 = int(first[:firstBreak])
        a2 = int(first[firstBreak+1:])

        b1 = int(second[:secondBreak])
        b2 = int(second[secondBreak+1:])

        # Everything above this was the same as Part One
        # below will be the same process but I break it into conditionals to be easier to read
        if a1 <= b1 and a2 >= b1:
            count += 1
        elif a1 <= b2 and a2 >= b2:
            count += 1
        elif b1 <= a1 and b2 >= a1:
            count += 1
        elif b1 <= a2 and b2 >= a2:
            count += 1


print(count)
