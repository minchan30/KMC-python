# 1부터 100까지
# 5의 배수 라면 출력
# 5번 출력했으면 개행

for i in range(1 , 101):    
    if i % 5 == 0:
        print(i , "" , end=' ')
    if i % 25 == 0:
        print()