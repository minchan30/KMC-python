a = int(input('첫 번쨰 시간의 시를 입력하세요 :'))
b = int(input('첫 번째 시간의 분을 입력하세요 :'))
c = int(input('두 번째 시간의 시를 입력하세요 :'))
d = int(input('두 번째 시간의 분을 입력하세요 :'))

if a > c :
    fastH = c
    fastM = d
    slowH = a
    slowM = b
elif a < c :
    fastH = a
    fastM = b
    slowH = c
    slowM = d
else :
    if b > d:
        fastH = c
        fastM = d
        slowH = b
        slowM = a
    else :
        fastH = a
        fastM = b
        slowH = c
        slowM = d

print("빠른시간 : ", fastH, ":", fastM, sep='')
print("늦은시간 : ", slowH, ":", slowM, sep='')