
# PART 1
# priority = 0
# with open("input.txt") as f:
#     for row in f:
#         firstHalf = row[:len(row)//2]
#         secondHalf = row[len(row)//2:]

#         for letter in firstHalf:
#             if letter in secondHalf:
#                 if letter >= "a":
#                     priority += ord(letter) - ord("a") + 1
#                 else:
#                     priority += ord(letter.lower()) - ord("a") + 27
#                 break

# print(priority)


# PART 2
priority = 0
with open("input.txt") as f:
    row1 = ""
    row2 = ""
    row3 = ""
    for row in f:
        if row1 == "":
            row1 = row
        elif row2 == "":
            row2 = row
        else:
            row3 = row

            # on 3rd row do stuff
            for letter in row1:
                if letter in row2 and letter in row3:
                    if letter >= "a":
                        priority += ord(letter) - ord("a") + 1
                    else:
                        priority += ord(letter.lower()) - ord("a") + 27
                    break

            row1 = ""
            row2 = ""
            row3 = ""

print(priority)
