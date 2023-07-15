i = 1
count = 0

while i <= 1000 :
    if i % 3 != 0 :
        print('%d' %i , end = ' ')
        
        count += 1 

        if count % 10 == 0 :
            print()

    i += 1