a = input('이름을 입력하세요 :')
b = input('일주일간 일한 시간을 입력하세요 :')
print()
print('-이름 :' , a)
print('-일주일간 일한 시간:' , int(b))

if int(b) > 40 :
    print('-오버타임 :' , int(b) - 40 , '시간')
    money = 40 * 12000 + (int(b) - 40) * 12000 * 1.5

else :   
    print('-오버타임 : 없음')
    money = int(b) * 12000

print('-주급 :' , money)
