# numbers = [7 , 9 , 15 , 18 , 30 , -3 , 7 , 12 , -16 , -12]

# sum = 0
# i = 1
# print('짝수 번째 요소 :' , end=" ")
# while i < len(numbers) :
#     sum += numbers[i]
#     print(numbers[i], end= " ")
#     i += 2

# print()
# print('합계 :' , sum)

# numbers = [7 , 9 , 15 , 18 , 30 , -3 , 7 , 12 , -16 , -12]
# myList = []

# i = 1
# while i < len(numbers):
#     myList.append(numbers[i])
#     i += 2

# print("짝수 번째 요소 : ", myList)
# print(sum(myList))

numbers = [7 , 9 , 15 , 18 , 30 , -3 , 7 , 12 , -16 , -12]
myList = []

for i in range(len(numbers)):
    if i % 2 == 1:
        myList.append(numbers[i])

print("짝수 번째 요소 : ", myList)
print(sum(myList))