print('-' * 35)
print('   cm    mm     m      inch')
print('-' * 35)

for cm in range(1 , 51) :
    mm = cm * 10
    m = cm * 0.01
    inch = cm * 0.3937
    print('   %d     %d    %.2f    %.2f' %(cm , mm , m , inch))

print('-' * 35)