with open('input.txt') as file:
  map = [line.rstrip() for line in file.readlines()]

visible = 0
highest_scenic_score = 0
Y, X = len(map), len(map[0])
for y in range(Y):
  for x in range(X):
    if y in [0, Y - 1] or x in [0, X - 1]:
      visible += 1
    else:
      is_visible = False
      scenic_score = 1
      # Top
      for y_top in range(y - 1, -1, -1):
        if map[y_top][x] >= map[y][x]:
          scenic_score *= (y - y_top)
          break
        if y_top == 0:
          is_visible = True
          scenic_score *= y
      # Left
      for x_left in range(x - 1, -1, -1):
        if map[y][x_left] >= map[y][x]:
          scenic_score *= (x - x_left)
          break
        if x_left == 0:
          is_visible = True
          scenic_score *= x
      # Right
      for x_right in range(x + 1, X):
        if map[y][x_right] >= map[y][x]:
          scenic_score *= (x_right - x)
          break
        if x_right == X - 1:
          is_visible = True
          scenic_score *= (X - x - 1)
      # Down
      for y_down in range(y + 1, Y):
        if map[y_down][x] >= map[y][x]:
          scenic_score *= (y_down - y)
          break
        if y_down == X - 1:
          is_visible = True
          scenic_score *= (Y - y - 1)
          
      visible += is_visible
      highest_scenic_score = max(highest_scenic_score, scenic_score)

print('Part 1:', visible)
print('Part 2:', highest_scenic_score)