with open('input.txt') as file:
  data = file.readline()

start_marker = ''
i = 0
LENGTH_OF_START_MARKER = 14 # 4
while len(start_marker) < LENGTH_OF_START_MARKER or len(set(start_marker)) != len(start_marker):
  start_marker += data[i]
  start_marker = start_marker[-LENGTH_OF_START_MARKER:]
  i += 1

# Part 1: 1920
# print('Part 1:', i)
print('Part 2:', i)