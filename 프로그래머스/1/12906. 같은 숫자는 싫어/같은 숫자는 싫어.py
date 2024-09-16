def solution(arr):
    answer = []
    
    for num in arr:
        if len(answer) > 0 and answer[-1] == num:
            continue
        else:
            answer.append(num)
    
    return answer