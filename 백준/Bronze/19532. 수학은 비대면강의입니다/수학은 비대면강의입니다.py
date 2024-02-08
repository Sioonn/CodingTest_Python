var = list(map(int, input().split()))
print(int((var[2]*var[4] - var[1]*var[5])/(var[0]*var[4] - var[1]*var[3])),
      int((var[2]*var[3]-var[0]*var[5])/(var[1]*var[3]-var[4]*var[0])))
