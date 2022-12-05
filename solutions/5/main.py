AMOUNT_OF_STACKS = 9

with open('input.txt') as file:
  lines = [line.rstrip() for line in file.readlines()]
  stacks = [[] for _ in range(AMOUNT_OF_STACKS)]
  for i in range(7, -1, -1):
    line = lines[i]
    for j in range(1, 8 * 4 + 2, 4):
      cand = line[j]
      if cand != ' ':
        stacks[j // 4].append(cand)

for i in range(10, len(lines)):
  line = lines[i]
  how_much, from_which, to_what = list(map(int, line.split()[1::2]))
  # for _ in range(how_much):
  #   stacks[to_what - 1].append(stacks[from_which - 1].pop())
  stacks[to_what - 1].extend(stacks[from_which - 1][-how_much:])
  stacks[from_which - 1] = stacks[from_which - 1][:-how_much]

# Part 1: CWMTGHBDW
# print('Part 1:', ''.join([stack[-1] for stack in stacks]))
print('Part 2:', ''.join([stack[-1] for stack in stacks]))