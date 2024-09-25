a, b = map(int, input().split())
result = []
for i in range(1, a * b + 1):
    if i % a == 0 and i % b == 0:
        result.append(3)
    elif i % a == 0:
        result.append(2)
    elif i % b == 0:
        result.append(1)
print("".join(map(str, result)))