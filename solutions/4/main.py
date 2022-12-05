with open('input.txt') as file:
  lines = [line.rstrip() for line in file.readlines()]

full_included = 0
part_overlap = 0
for line in lines:
  a, b = line.split(',')
  [b1, e1], [b2, e2] = list(map(int, a.split('-'))), list(map(int, b.split('-')))
  if b1 <= b2 <= e1 and b1 <= e2 <= e1 or b2 <= b1 <= e2 and b2 <= e1 <= e2:
    full_included += 1
  if b1 <= b2 <= e1 or b1 <= e2 <= e1 or b2 <= b1 <= e2 or b2 <= e1 <= e2:
    part_overlap += 1

print('Part 1:', full_included)
print('Part 2:', part_overlap)