input_str = input()
combination = list(input_str)
for i in range(2,len(input_str)+1):
    for j in range(len(input_str)-i+1):
        combination.append(input_str[j:j+i])

print(len(set(combination)))