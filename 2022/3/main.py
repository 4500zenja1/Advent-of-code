with open('input.txt') as file:
  rucksacks = [rucksack.rstrip() for rucksack in file.readlines()]

res_1 = 0
res_2 = 0
priority = lambda c: ord(c.lower()) - ord('a') + 1 + 26 * c.isupper()
id_badges = {}
index = 0
for rucksack in rucksacks:
  badges = set(list(rucksack))
  if index % 3 == 0:
    id_badges = badges

  l = len(rucksack)
  a, b = set(list(rucksack[:l // 2])), set(list(rucksack[l // 2:]))
  common = a & b
  id_badges &= badges
  
  res_1 += priority(next(iter(common)))
  if index % 3 == 2:
    res_2 += priority(next(iter(id_badges)))
  index += 1

print('Part 1:', res_1)
print('Part 2:', res_2)