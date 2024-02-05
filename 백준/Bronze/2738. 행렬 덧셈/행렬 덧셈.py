n,m = map(int,input().split())
matrix_1 = []
matrix_2 = []
for _ in range(n):
  matrix_1.append(input().split())
for _ in range(n):
  matrix_2.append(input().split())

result_matrix = [[0]*m for _ in range(n)]
for i in range(n):
  for j in range(m):
    result_matrix[i][j] = int(matrix_1[i][j]) + int(matrix_2[i][j])

for i in range(n):
  for j in range(m):
    print(result_matrix[i][j], end=" ")
  print(end='\n')