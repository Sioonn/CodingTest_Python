N = int(input())
owned_card = list(map(int, input().split()))
M = int(input())
given_card = list(map(int, input().split()))
result = [0]*M
owned_card.sort()

for i in range(len(given_card)):
    start,end = 0,N-1
    while (start <= end):
        mid = (start+end)//2
        if given_card[i] > owned_card[mid]:
            start = mid + 1
        elif given_card[i] < owned_card[mid]:
            end = mid - 1
        else:
            result[i] = 1
            break

print(*result)