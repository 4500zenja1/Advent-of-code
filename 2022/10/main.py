X = 1

with open('input.txt') as file:
  lines = [line.rstrip() for line in file.readlines()]

loop_count = 0
sum_of_X = 0
curr_target = 20

for line in lines:
  if line == 'noop':
    sum_of_X += X * (loop_count % 40 == 19) * curr_target
    loop_count += 1
  else:
    sum_of_X += X * (18 <= loop_count % 40 <= 19) * curr_target
    loop_count += 2
    X += int(line[5:])
  if loop_count >= curr_target:
    curr_target += 40

print('Sum of each 40th X, starting with 20, is', sum_of_X, '\n')

GRID_LENGTH = 40
GRID_HEIGHT = 6
grid = ['' for _ in range(GRID_HEIGHT)]
sprite_indexes = [0, 1, 2]
y, x = 0, 0

for line in lines:
  for _ in range(1 + (line[:4] == 'addx')):
    grid[y] += '#' if x in sprite_indexes else '.'
    x += 1
    y, x = y + x // GRID_LENGTH, x % GRID_LENGTH
  if line[:4] == 'addx':
    sprite_indexes = [i + int(line[5:]) for i in sprite_indexes]

print('\n'.join([row for row in grid]))