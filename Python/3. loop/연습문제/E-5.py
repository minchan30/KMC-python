sum = 0
i = 4

while i <= 100 :
    if i % 4 == 0 :
        sum += i
        print('%d --> %d' % (i , sum))
    i = i + 1