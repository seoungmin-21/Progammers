def solution(n, lost, reserve):
    
    student_list = list(range(1, n + 1))
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    answer = n - len(lost_set)
    
    for i in student_list:
        if i in lost_set:
            if (i - 1) in reserve_set:
                reserve_set.remove(i - 1)
                answer += 1
            elif (i + 1) in reserve_set:
                reserve_set.remove(i + 1)
                answer += 1
                
    return answer