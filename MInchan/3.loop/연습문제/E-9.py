print('-' * 35)
print('   cm    mm     m      inch')
print('-' * 35)

cm = 1

while cm <= 50 :
    mm = cm * 10
    m = cm * 0.01
    inch = cm * 0.3937

    print('   %d     %d    %.2f    %.2f' %(cm , mm , m , inch))

    cm += 1

print('-' * 35)