# 2차원 리스트로 문자열 다루기
strings = [['원두커피' , '라떼' , '콜라'] , ['우동' , '국수' , '피자' , '파스타']]

for i in range(len(strings)) :
    for j in range(len(strings[i])) :
        print(strings[i][j])

# 실행결과
# 원두커피
# 라떼
# 콜라
# 우동
# 국수
# 피자
# 파스타