# PART ONE
# file = open("input.txt")
# signal = file.readline()
# count = 4
# for i in range(4, len(signal)):
#     curr_four = [i for i in signal[i-4:i]]
#     four_set = set(curr_four)
#     if len(four_set) == len(curr_four):
#         break
#     count += 1


# print("PART ONE:", count)


# PART TWO
file = open("input.txt")
signal = file.readline()
count = 14
for i in range(14, len(signal)):
    curr_four = [i for i in signal[i-14:i]]
    four_set = set(curr_four)
    if len(four_set) == len(curr_four):
        break
    count += 1


print("PART TWO:", count)
