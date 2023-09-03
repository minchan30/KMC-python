temp = {'월' : 15.5 , '화' : 17.0 , '수' : 16.2 , '목' : 12.9 , '금' : 11.0 , '토' : 10.5 , '일' : 13.3}

print('-' * 46)
print(' 월     화     수     목     금     토     일')
print('-' * 46)
for key in temp :
    print(temp[key], end='   ')

print()
print('-' * 46)