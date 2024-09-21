li = [list('.' * 20) for _ in range(10)]
for _ in range(int(input())):
    s = input()
    li[ord(s[0]) - ord('A')][int(s[1:]) - 1] = 'o'
for i in range(10):
    for j in range(20):
        print(li[i][j], end='')
    print()