N,M = map(int,input().split())
owned_string,given_string = [],[]
for _ in range(N):
    owned_string.append(input())
for _ in range(M):
    given_string.append(input())

print(len([i for i in given_string if i in owned_string]))