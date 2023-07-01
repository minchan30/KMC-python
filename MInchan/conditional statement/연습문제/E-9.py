score = int(input('점수를 입력하세요 :'))

if 90 <= score <= 100 :
    print('- 성적 :', score, ',등급 : 수')

elif 80 <= score <= 89  :
    print('- 성적 :', score, ',등급 :  우')

elif 70 <= score <= 79  :
    print('- 성적 :', score, ',등급 :  미')

elif 60 <= score <= 69  :
    print('- 성적 :', score, ',등급 :  양')

elif 0 <= score <= 59  :
    print('- 성적 :', score, ',등급 :  가')

else :
    print('입력 오류!')