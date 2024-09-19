def solution(array, commands):
    answer = []
    NewList = []
    
    for i in commands:
        NewList = array[i[0]-1:i[1]]
        NewList.sort()
        answer.append(NewList[i[2]-1])
    
    return answer