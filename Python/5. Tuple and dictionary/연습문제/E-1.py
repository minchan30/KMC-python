year_sale = {'2016' : 237 , '2017' : 98 , '2018' : 158 , '2019' : 233 , '2020' : 120}

for key in year_sale :
    if key == '2017' :
        print('%s년 자동차 판매량 : %d대' % (key , year_sale[key]))