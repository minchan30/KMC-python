# 2차원 리스트의 이중 for문
data = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]

for i in range(4) :
    for j in range(2) :
        print('data[%d][%d] = %d' % (i , j , data[i][j]))

# 실행결과
# data[0][0] = 10
# data[0][1] = 20
# data[1][0] = 30
# data[1][1] = 40
# data[2][0] = 50
# data[2][1] = 60
# data[3][0] = 70
# data[3][1] = 80