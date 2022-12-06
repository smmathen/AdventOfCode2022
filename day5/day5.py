from math import ceil

# file = open("input.txt")

# # make 9 stacks
# stacks = [[] for i in range(9)]
# # first 8 lines are the stack
# for _ in range(8):
#     line = file.readline()
#     # 0-2 belong to 1, 4-6 belong to 2, 7-9 belong to 3
#     for j in range(len(line)):
#         char = line[j]
#         if char >= "A" and char <= "Z":
#             stack = stacks[ceil(j/4)-1]
#             stack.append(char)

# # skip next two lines
# for _ in range(2):
#     file.readline()

# line = file.readline()
# while line:

#     count = int(line[line.find(" ") + 1: line.find("f")-1])
#     start = int(line[line.find("from") + 5: line.find("t") - 1])-1
#     end = int(line[line.rfind(" ") + 1:])-1

#     while count > 0:
#         to_move = stacks[start].pop(0)
#         stacks[end].insert(0, to_move)
#         count -= 1

#     line = file.readline()

# file.close()

# to_return = ""
# for stack in stacks:
#     to_return += stack[0]

# print("PART ONE:", to_return)
file = open("input.txt")

# make 9 stacks
stacks = [[] for i in range(9)]
# first 8 lines are the stack
for _ in range(8):
    line = file.readline()
    # 0-2 belong to 1, 4-6 belong to 2, 7-9 belong to 3
    for j in range(len(line)):
        char = line[j]
        if char >= "A" and char <= "Z":
            stack = stacks[ceil(j/4)-1]
            stack.append(char)

# skip next two lines
for _ in range(2):
    file.readline()

line = file.readline()
while line:

    count = int(line[line.find(" ") + 1: line.find("f")-1])
    start = int(line[line.find("from") + 5: line.find("t") - 1])-1
    end = int(line[line.rfind(" ") + 1:])-1

    to_move = []
    for _ in range(count):
        to_move.append(stacks[start].pop(0))

    while count > 0:
        stacks[end].insert(0, to_move.pop())
        count -= 1

    line = file.readline()

file.close()

to_return = ""
for stack in stacks:
    to_return += stack[0]


print("PART TWO:", to_return)
