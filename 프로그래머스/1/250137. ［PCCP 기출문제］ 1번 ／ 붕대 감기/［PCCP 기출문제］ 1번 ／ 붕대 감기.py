def solution(bandage, health, attacks):
    bonus_time, rec_per_sec, bonus_rec = bandage
    present_health = health
    prev_time = 0
    
    for time,attack in attacks:
        time_gap = time - prev_time - 1
        bonus_health = time_gap * rec_per_sec + (time_gap // bonus_time) * bonus_rec
        present_health += bonus_health
        if present_health >= health:
            present_health = health

        if present_health - attack <= 0:
            return -1
        else:
            present_health -= attack
            
        prev_time = time
        
    answer = present_health
        
    return answer