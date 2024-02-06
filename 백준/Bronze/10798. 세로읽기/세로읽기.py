row = 5
max_col = 0

input_list = []
for _ in range(row):
  each_list = list(input())
  max_col = max(max_col, len(each_list))
  input_list.append(each_list)

for each_list in input_list:
  if len(each_list) < max_col:
    while(len(each_list) != max_col):
      each_list.append(-1)
  else:
    max_col = len(each_list)

for i in range(max_col):
  for j in range(row):
    if input_list[j][i] != -1:
      print(input_list[j][i],end='')