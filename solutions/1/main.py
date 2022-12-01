with open('input.txt') as file:
  calories = [line.rstrip() for line in file]

curr_calories = 0
calories_lst = []
for calorie in calories:
  if calorie:
    curr_calories += int(calorie)
  else:
    calories_lst.append(curr_calories)
    curr_calories = 0

calories_lst.sort(reverse=True)
print(calories_lst[0], sum(calories_lst[:3]))