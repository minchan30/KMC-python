sum = 0
for i in range(1 , 101) :
    if i % 3 == 0 :
        sum = sum + i

# 1 : X
# 2 : X
# 3 : sum = 0 + 3
# 4 : X
# 5 : X
# 6 : sum = 3 + 6
# 7 : X
# 8 : X
# 9 : sum = 9 + 9

print('1 ~ 100 까지의 3의 배수 합계 : %d' % sum)