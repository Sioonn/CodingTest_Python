def solution(cap,n,deliveries,pickups):
    result = n
    deliveries.reverse()
    pickups.reverse()
    del_accum, pick_accum = 0,0
    accum_reverse_deliveries,accum_reverse_pickups = [],[]
    for i in range(n):
        del_accum += deliveries[i]
        pick_accum += pickups[i]
        if del_accum == 0 and pick_accum == 0:
            result -= 1
        del_accum_item = (del_accum // cap) + (del_accum % cap) / 100
        pick_accum_item = (pick_accum // cap) + (pick_accum % cap) / 100
        accum_reverse_deliveries.append(del_accum_item)
        accum_reverse_pickups.append(pick_accum_item)
    
    max_item = [0]+[max(accum_reverse_deliveries[i], accum_reverse_pickups[i]) for i in range(n)]
    for i in range(len(max_item)):
        if max_item[i] != 0 and max_item[i] == int(max_item[i]):
            max_item[i] -= 0.01
    
    for i in range(1,n+1):
        cnt = 0
        cnt += int(max_item[i]) - int(max_item[i-1])
        result += (n-i+1)*cnt

    return 2*result