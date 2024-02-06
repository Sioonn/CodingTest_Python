up,down,length = map(int,input().split())
if (length-up)%(up-down) == 0:
  print((length-up) // (up-down) + 1)
else:
  print((length-up) // (up-down) + 2)