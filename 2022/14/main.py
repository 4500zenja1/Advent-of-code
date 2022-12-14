from copy import deepcopy

HEIGHT = WIDTH = 0
RESERVE = 2
OFFSET = 1000

points_lsts = []

with open('input.txt') as file:
  lines = [line.rstrip() for line in file.readlines()]
  for line in lines:
    points = line.split(' -> ')
    points_lsts.append([])
    for point in points:
      [X, Y] = list(map(int, point.split(',')))
      points_lsts[-1].append([X, Y])
      HEIGHT = max(HEIGHT, Y)
      WIDTH = max(WIDTH, X)

map_p1 = [['.' for _ in range(WIDTH + RESERVE + OFFSET)] for _ in range(HEIGHT + RESERVE)]
for points_lst in points_lsts:
  [X_curr, Y_curr] = points_lst[0]
  for i in range(1, len(points_lst)):
    [X_new, Y_new] = points_lst[i]
    X_min, X_max = min(X_curr, X_new), max(X_curr, X_new)
    Y_min, Y_max = min(Y_curr, Y_new), max(Y_curr, Y_new)
    for X in range(X_min, X_max+1):
      for Y in range(Y_min, Y_max+1):
        map_p1[Y][X] = '#'
    X_curr, Y_curr = X_new, Y_new

map_p2 = deepcopy(map_p1)

sand_to_rest = 0
is_not_falling_into_void = True
while is_not_falling_into_void:
  [X, Y] = [500, 0]
  while True:
    if map_p1[Y+1][X] == '.':
      Y += 1
    elif map_p1[Y+1][X-1] == '.':
      Y += 1
      X -= 1
    elif map_p1[Y+1][X+1] == '.':
      Y += 1
      X += 1
    else:
      map_p1[Y][X] = '#'
      sand_to_rest += 1
      break
    if Y >= HEIGHT:
      is_not_falling_into_void = False
      break

print('Part 1:', sand_to_rest)

sand_to_rest = 0
[X, Y] = [500, 0]
is_sand_in_move = False

while True:
  is_sand_in_move = True
  if Y - HEIGHT + 1 == RESERVE:
    map_p2[Y][X] = '#'
    sand_to_rest += 1
    is_sand_in_move = False
  elif map_p2[Y+1][X] == '.':
    Y += 1
  elif map_p2[Y+1][X-1] == '.':
    Y += 1
    X -= 1
  elif map_p2[Y+1][X+1] == '.':
    Y += 1
    X += 1
  else:
    map_p2[Y][X] = '#'
    sand_to_rest += 1
    is_sand_in_move = False
  if not is_sand_in_move:
    if [X, Y] == [500, 0]:
      break
    [X, Y] = [500, 0]

print('Part 2:', sand_to_rest)