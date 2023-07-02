word = input('영어 문장을 입력하세요 :')

for x in word :
    print(x)

#실행결과

#I

#a
#m

#h
#a
#p
#p
#y
#!

phone = input('하이픈(-)을 포함한 휴대폰 번호를 입력하세요:')

for x in phone :
    if x != "-" :
        print('%s' % x , end = "")

# 실행결과

# 하이픈(-)을 포함한 휴대폰 번호를 입력하세요:010-3523-1629
# 0103523162