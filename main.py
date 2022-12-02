with open('input.txt') as file:
  lines = [line.rstrip() for line in file.readlines()]

points = {'X': 1, 'Y': 2, 'Z': 3}
win = {'C': 'X', 'A': 'Y', 'B': 'Z'}
draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
lose = {'B': 'X', 'C': 'Y', 'A': 'Z'}

score_1 = 0
score_2 = 0
for line in lines:
  opponent_turn, my_turn = line.split()
  score_1 += points[my_turn] + 6 * (win[opponent_turn] == my_turn) + 3 * (draw[opponent_turn] == my_turn)

  my_turn = [lose[opponent_turn], draw[opponent_turn], win[opponent_turn]][ord(my_turn) - ord('X')]
  score_2 += points[my_turn] + 6 * (win[opponent_turn] == my_turn) + 3 * (draw[opponent_turn] == my_turn)

print('Part 1:', score_1)
print('Part 2:', score_2)