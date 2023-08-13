hello = 'have a nice day'
print(hello)

list1 = hello.split(' ')
print(list1)
print(type(list1))

for i in range(0 , len(list1)) :
    print('list1[%d] : %s' %(i , list1[i]))

# 실행결과
# have a nice day
# ['have', 'a', 'nice', 'day']
# <class 'list'>
# list1[0] : have
# list1[1] : a
# list1[2] : nice
# list1[3] : day