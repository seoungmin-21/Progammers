def solution(numbers):
    
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*10, reverse=True)
    
    return str(int("".join(map(str,numbers))))