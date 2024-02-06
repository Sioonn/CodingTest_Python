# 최댓값 찾기
input_list = []
for _ in range(9):
  input_list.append(list(map(int, input().split())))

max=-1
max_row=0
max_col=0
for i in range(len(input_list)):
  for j in range(len(input_list[i])):
    if (input_list[i][j] > max):
      max_row = i + 1
      max_col = j + 1
      max = input_list[i][j]

print(max)
print(max_row, max_col)
