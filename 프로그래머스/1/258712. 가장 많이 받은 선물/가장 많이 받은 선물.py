def solution(friends, gifts):
    num_friends = len(friends)
    present_list = [[0 for _ in range(num_friends)]  for _ in range(num_friends)]
    friend_dict = {key:value for value,key in enumerate(friends)}
    
    for i in gifts:
        give_present, receive_present = i.split()
        present_list[friend_dict[give_present]][friend_dict[receive_present]] += 1

    present_idx = dict()
    for i in range(len(friends)):
        total_give = sum([give for give in present_list[i]])
        
        total_receive = sum([present_list[j][i] for j in range(len(friends))])
        present_idx[friends[i]] = total_give - total_receive

    result = [0 for _ in range(len(friends))]
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i!=j and present_list[i][j] == present_list[j][i]:
                if present_idx[friends[i]] > present_idx[friends[j]]:
                    result[i] += 1
            else:
                if i!=j and present_list[i][j] > present_list[j][i]:
                    result[i] += 1
                    
    answer = max(result)

    return answer