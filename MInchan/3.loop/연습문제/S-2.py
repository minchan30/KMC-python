flag = True

while flag:
    score = int(input('성적을 입력하세요 :'))
    if score >= 90 :
        grade = '수'
    elif score >=80 :
        grade = '우'
    elif score >= 70 :
        grade = '미'
    elif score >= 60 :
        grade = '양'
    else :
        grade = '가'
    print('등급 :' , grade)

    cont = input("계속하시겠습니까 (중단: q , 계속: y) :")
    if cont != 'y':
        flag = False