from queue import Queue

with open('input.txt') as file:
  lines = [line.rstrip() for line in file.readlines()]

monkey_items = []
monkey_mod = []
monkey_operation = []
monkey_test = []
monkey_if_true = []
monkey_if_false = []

line_num = 0
BLOCK_SIZE = 7

for line in lines:
  if line_num == 0:
    monkey_items.append([])
  elif line_num == 1:
    items = list(map(int, line.split(': ')[1].split(', ')))
    for item in items:
      monkey_items[-1].append(item)
  elif line_num == 2:
    [op, val] = line.split()[-2:]
    monkey_operation.append([op, val])
  elif line_num == 3:
    monkey_test.append(int(line.split()[-1]))
  elif line_num == 4:
    monkey_if_true.append(int(line.split()[-1]))
  elif line_num == 5:
    monkey_if_false.append(int(line.split()[-1]))
    
  line_num = (line_num + 1) % BLOCK_SIZE

for items in monkey_items:
  monkey_mod.append(Queue())
  for item in items:
    mod_dict = {}
    for t in monkey_test:
      mod_dict[t] = item % t
    monkey_mod[-1].put(mod_dict)

TURNS = 10000 # 2
monkey_inspection_count = [0 for _ in range(len(monkey_items))]

for turn in range(TURNS):
  for i in range(len(monkey_mod)):
    q = monkey_mod[i]
    while not q.empty():
      mod_queue = q.get()
      op, val = monkey_operation[i]
      for m in mod_queue:
        mod_val = mod_queue[m]
        new_val = mod_val if val == 'old' else int(val)
        if op == '*':
          mod_queue[m] = (new_val * mod_val) % m
        else:
          mod_queue[m] = (new_val + mod_val) % m

      test, monkey_true, monkey_false = monkey_test[i], monkey_if_true[i], monkey_if_false[i]

      if mod_queue[test] == 0:
        monkey_mod[monkey_true].put(mod_queue)
      else:
        monkey_mod[monkey_false].put(mod_queue)

      monkey_inspection_count[i] += 1
      
[first, second] = sorted(monkey_inspection_count, reverse=True)[:2]

# The solution above is for Part 2,
# for Part 1 you can just take items as they are,
# without modulos and such
#
# Part 1: 54253
# print('Part 1:', first * second)
print('Part 2:', first * second)