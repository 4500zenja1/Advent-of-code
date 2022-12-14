with open('input.txt') as file:
  lines = file.read().strip().split('\n')

ROPE_LENGTH = 9 + 1 # including the head, part 1: 1 + 1
rope = [[0, 0] for _ in range(ROPE_LENGTH)]
tail_visited = {tuple([0, 0])}

def axis_distance(x1, y1, x2, y2):
  return max(abs(x1 - x2), abs(y1 - y2))

for line in lines:
  direction, n = line.split()
  for _ in range(int(n)):
    if direction == 'U':
      rope[0][1] += 1
    elif direction == 'R':
      rope[0][0] += 1
    elif direction == 'D':
      rope[0][1] -= 1
    elif direction == 'L':
      rope[0][0] -= 1

    for i in range(1, ROPE_LENGTH):
      [x_prev, y_prev], [x_curr, y_curr] = rope[i-1], rope[i]
      if axis_distance(x_prev, y_prev, x_curr, y_curr) > 1:
        if y_prev == y_curr and x_prev - x_curr > 1:
          x_curr += 1
        elif y_prev == y_curr and x_prev - x_curr < -1:
          x_curr -= 1
        elif x_prev == x_curr and y_prev - y_curr > 1:
          y_curr += 1
        elif x_prev == x_curr and y_prev - y_curr < -1:
          y_curr -= 1

        elif x_prev > x_curr and y_prev > y_curr:
          x_curr += 1
          y_curr += 1
        elif x_prev > x_curr and y_prev < y_curr:
          x_curr += 1
          y_curr -= 1
        elif x_prev < x_curr and y_prev > y_curr:
          x_curr -= 1
          y_curr += 1
        elif x_prev < x_curr and y_prev < y_curr:
          x_curr -= 1
          y_curr -= 1
      rope[i] = [x_curr, y_curr]
    
    tail_visited.add((x_curr, y_curr))

# Part 1: 5874
# print('Part 1:', len(tail_visited))
print('Part 2:', len(tail_visited))