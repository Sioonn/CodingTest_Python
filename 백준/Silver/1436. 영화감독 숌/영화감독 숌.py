input_num = int(input())
cnt = 0
num = 666
result = 0
while True:
    if '666' in str(num):
        cnt += 1
    if cnt == input_num:
        result = cnt
        break
    num += 1

print(num)