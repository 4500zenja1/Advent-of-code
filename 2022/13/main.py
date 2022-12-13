from ast import literal_eval
with open('input.txt') as file:
  lines = [literal_eval(line.rstrip()) for line in file.readlines() if line != '\n']

def cmp(a, b):
  if isinstance(a, int) and isinstance(b, int):
    return (a > b) - (a < b)
  if isinstance(a, int) and isinstance(b, list):
    return cmp([a], b)
  if isinstance(a, list) and isinstance(b, int):
    return cmp(a, [b])
  if isinstance(a, list) and isinstance(b, list):
    for val in map(cmp, a, b):
      if val:
        return val
    return cmp(len(a), len(b))

sum_of_right = 0
for i in range(0, len(lines), 2):
  a, b = lines[i], lines[i+1]
  if cmp(a, b) == -1:
    sum_of_right += i // 2 + 1

print('Part 1:', sum_of_right)

add_lst = [ [[2]], [[6]] ]
lines.extend(add_lst)
for i in range(len(lines)):
  for j in range(i + 1, len(lines)):
    if cmp(lines[i], lines[j]) == 1:
      lines[i], lines[j] = lines[j], lines[i]

print('Part 2:', (lines.index(add_lst[0]) + 1) * (lines.index(add_lst[1]) + 1))