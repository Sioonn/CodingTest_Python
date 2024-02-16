# 시간초과 
def update_lists(box_list,cap):
    for i in range(len(box_list)):
        if box_list[i] >= cap:
            box_list[i] -= cap
            return box_list
        else:
            cap -= box_list[i]
            box_list[i] = 0
    return [0]*len(box_list)

def solution(cap, n, deliveries, pickups):
    deliveries.reverse()
    pickups.reverse()
    answer = 0
    start = n-1

    while sum(deliveries) + sum(pickups) != 0:
        for i in range(n):
            if deliveries[i] != 0 or pickups[i] != 0:
                start = i
                break

        deliveries = update_lists(deliveries,cap)
        pickups = update_lists(pickups,cap)        
        answer += 2*(n-start)
    return answer
