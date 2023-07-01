x = input('문자열을 입력하세요 :')

n = len(x)
print('문자열의 개수 :' , str(n))

if n % 2 == 0 :
    print('문자열의 개수는 짝수이다.')

else :
    print('문자열의 개수는 홀수이다.')