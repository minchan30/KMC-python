num = int(input('시작 수를 입력해주세요 :'))
num2 = int(input('끝 수를 입력하세요 :'))

for k in range(num, num2+1):
    flag = True
    for i in range(2, k//2):
        if k % i == 0:
            flag = False
            break

    if flag == True:
        print(k,end = " ")
