def solution(s):
    answer = True
    stack = []
    
    for char in s:
        if len(stack) > 0 and stack[-1] != char:
            if stack[-1] == ")" and char == "(":
                stack.append(char)
            else:
                stack.pop()
        else:
            stack.append(char)
        
    if not stack:
        answer = True
    else:
        answer = False
    
    return answer