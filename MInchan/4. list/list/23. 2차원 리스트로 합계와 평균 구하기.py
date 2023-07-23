# 2차원 리스트로 성적 합계와 평균 구하기
scores = [[75 , 83 , 90] , [86 , 86 , 73] , [76 , 95 , 83] , [89 , 96 , 69] , [86 , 79 , 93]]

for i in range(len(scores)) :
    sum = 0
    for j in range(len(scores[i])) :
        sum = sum + scores[i][j]

    avg = sum / len(scores[i])

    print('%d번쨰 학생의 합계 : %d , 평균 : %.2f' % (i + 1 , sum , avg))

# 실행결과
# 1번쨰 학생의 합계 : 248 , 평균 : 82.67
# 2번쨰 학생의 합계 : 245 , 평균 : 81.67
# 3번쨰 학생의 합계 : 254 , 평균 : 84.67
# 4번쨰 학생의 합계 : 254 , 평균 : 84.67
# 5번쨰 학생의 합계 : 258 , 평균 : 86.00