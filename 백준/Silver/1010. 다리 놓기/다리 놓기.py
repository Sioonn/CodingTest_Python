n = int(input())
input_list = []
for _ in range(n):
    a,b = map(int,input().split())
    input_list.append((a,b))

def facto(x):
    c = 1
    for i in range(1,x+1):
        c = c*i
    return c

def combi(a,b):
    return int(facto(b)/(facto(a) * facto(b-a)))

for a,b in input_list:
    print(combi(a,b))
    