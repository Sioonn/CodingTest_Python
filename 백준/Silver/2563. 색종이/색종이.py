graph_paper = [[0 for _ in range(100)] for _ in range(100)]

paper_num = int(input())
for _ in range(paper_num):
  x,y = map(int,input().split())
  for i in range(x,10+x):
    for j in range(y,10+y):
      if graph_paper[i][j] != 1:
        graph_paper[i][j] = 1

print(sum(graph_paper,[]).count(1))