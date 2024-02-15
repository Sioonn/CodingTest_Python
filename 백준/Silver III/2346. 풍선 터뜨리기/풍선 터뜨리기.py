N = int(input())
num_list = list(map(int,input().split()))
cursor = 0
result = []
remain = len(num_list)

while True:
    result.append(cursor+1)
    prev_cursor = cursor
    cnt = num_list[cursor]
    num_list[prev_cursor] = 1001
    remain -= 1
    
    if remain == 0:
        break

    while cnt:
        if cnt > 0:
            cursor = (cursor+1) % len(num_list)
            if num_list[cursor] != 1001:
                cnt -= 1
        else:
            cursor = (cursor-1) % len(num_list)
            if num_list[cursor] != 1001:
                cnt += 1

print(*result)