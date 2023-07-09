sum = 0
i = 500 

while i <= 600 :
    if i % 5 == 0 :
        sum+=i
        print(sum)
    i = i + 1

print('5의 배수 합계 : %d' %(sum))

# 실행결과
# 5의 배수 합계 : 11550