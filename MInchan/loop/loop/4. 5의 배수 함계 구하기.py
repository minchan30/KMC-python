sum = 0

for i in range(100 , 201 , 5) :
    sum = sum + i

print('5의 배수의 합계 : %d' % sum)

# 실행결과

# 5의 배수의 합계 : 3150

sum = 0
for i in range(100 , 201 ) :
    if i % 5 == 0 :
        sum = sum + i

print('5의 배수의 합계 : %d' % sum)

#실행결과

# 5의 배수의 합계 : 3150