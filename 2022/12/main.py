with open('input.txt') as file:
  map = [list(line.rstrip()) for line in file.readlines()]
  WIDTH, HEIGHT = len(map[0]), len(map)

def check(pos, new_pos):
  y_curr, x_curr = pos // WIDTH, pos % WIDTH
  y_new, x_new = new_pos // WIDTH, new_pos % WIDTH
  curr_pos, new_pos = map[y_curr][x_curr], map[y_new][x_new]
  return ord(new_pos) - ord(curr_pos) <= 1

# the map's position will be encoded with formula y * WIDTH + x
start = finish = 0
starting_positions = []
for y in range(len(map)):
  if 'S' in map[y]:
    x = map[y].index('S')
    start = y * WIDTH + x
    map[y][x] = 'a'
  if 'E' in map[y]:
    x = map[y].index('E')
    finish = y * WIDTH + x
    map[y][x] = 'z'
  starting_positions.append(y * WIDTH)

min_fewest_steps = float('inf')

for start_pos in starting_positions:
  fewest_steps = {start_pos: 0}
  positions = [start_pos]
  curr_steps = 0
  while positions:
    curr_steps += 1
    new_positions = []
    for pos in positions:
      y, x = pos // WIDTH, pos % WIDTH
      if y > 0:
        new_pos = (y - 1) * WIDTH + x
        if check(pos, new_pos) and (new_pos not in fewest_steps or fewest_steps[new_pos] > curr_steps):
          if new_pos not in fewest_steps:
            new_positions.append(new_pos)
          fewest_steps[new_pos] = curr_steps
      if x < WIDTH - 1:
        new_pos = y * WIDTH + (x + 1)
        if check(pos, new_pos) and (new_pos not in fewest_steps or fewest_steps[new_pos] > curr_steps):
          if new_pos not in fewest_steps:
            new_positions.append(new_pos)
          fewest_steps[new_pos] = curr_steps
      if y < HEIGHT - 1:
        new_pos = (y + 1) * WIDTH + x
        if check(pos, new_pos) and (new_pos not in fewest_steps or fewest_steps[new_pos] > curr_steps):
          if new_pos not in fewest_steps:
            new_positions.append(new_pos)
          fewest_steps[new_pos] = curr_steps
      if x > 0:
        new_pos = y * WIDTH + (x - 1)
        if check(pos, new_pos) and (new_pos not in fewest_steps or fewest_steps[new_pos] > curr_steps):
          if new_pos not in fewest_steps:
            new_positions.append(new_pos)
          fewest_steps[new_pos] = curr_steps
    if finish in new_positions:
      break
    else:
      positions = new_positions.copy()

  if start == start_pos:
    print('Part 1:', fewest_steps[finish])
  if finish in fewest_steps:
    min_fewest_steps = min(min_fewest_steps, fewest_steps[finish])

print('Part 2:', min_fewest_steps)