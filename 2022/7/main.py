from collections import defaultdict

files = defaultdict(dict)
subdirectories = defaultdict(list)
directory_sizes = {}

SIZE_LIMIT = 100000
part_1_res = 0

with open('input.txt') as file:
  lines = [line.rstrip() for line in file.readlines()]

curr_directory = '/'
line_index = 1
while line_index < len(lines):
  data = lines[line_index].split()
  if data[0] == '$':
    if data[1] == 'cd':
      if data[2] == '..':
        directory_size = 0
        for file_size in files[curr_directory].values():
          directory_size += file_size
        for subdirectory in subdirectories[curr_directory]:
          directory_size += directory_sizes[subdirectory]
        directory_sizes[curr_directory] = directory_size
        if directory_size <= SIZE_LIMIT:
          part_1_res += directory_size
        
        curr_directory = curr_directory[:curr_directory.rindex('/')]
      else:
        curr_directory += f'/{data[2]}'
  else:
    if data[0] == 'dir':
      subdirectories[curr_directory].append(curr_directory + f'/{data[1]}')
    else:
      file = f'curr_directory/{data[1]}'
      files[curr_directory][file] = int(data[0])
  line_index += 1

print('Part 1:', part_1_res)

# for Part 2, I need to get out of the outermost directory to get its size, so two lines '$ cd ..' were added to input.txt =P

TOTAL_AVAILABLE = 70000000
CURRENTLY_AVAILABLE = TOTAL_AVAILABLE - directory_sizes['/']
NEEDS_TO_BE_AVAILABLE = 30000000
NEEDS_TO_BE_DELETED = NEEDS_TO_BE_AVAILABLE - CURRENTLY_AVAILABLE

part_2_res = TOTAL_AVAILABLE
for cand_size in directory_sizes.values():
  if cand_size >= NEEDS_TO_BE_DELETED and cand_size < part_2_res:
    part_2_res = cand_size

print('Part 2:', part_2_res)