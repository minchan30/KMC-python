#리스트 새로운 요소 추가
arr = [5 , 3 , 12 , 9 , 2]
print(arr)


arr.append(10)
print(arr)

# 실행결과
# [5, 3, 12, 9, 2]
# [5, 3, 12, 9, 2, 10]


# 빈 리스트에 요소 추가
scores = []


while True :
    score = int(input('성적을 입력하세요(종료 : -1) :'))


    if score == -1 :
        break
    else :
        scores.append(score)

print(scores)

# 실행결과
# [95, 88, 76]