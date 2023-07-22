# replace( ) 메소드로 문자열 치환하기
string1 = '사과는 맛있다. 나는 사과를 제일 좋아한다.'
print(string1)

x = string1.replace('사과' , '딸기')
print(x)

# 실행결과
# 사과는 맛있다. 나는 사과를 제일 좋아한다.
# 딸기는 맛있다. 나는 딸기를 제일 좋아한다.

# 전화번호에서 하이픈 삭제하기
phone1 = '010-3523-1629'
print(phone1)

phone2 = phone1.replace('-' , "")
print(phone2)

# 실행결과
# 010-3523-1629
# 01035231629