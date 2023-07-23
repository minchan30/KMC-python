# 리스트 문자열에서 문자 치환하기
sentences = ['Love me, love my dog.' , 'No news is good news.' ,
            'Blood is thicker than water']

for sentence in sentences :
    x = sentence.replace(" " , "_")
    print(x)

# 실행결과
# Love_me,_love_my_dog.
# No_news_is_good_news.
# Blood_is_thicker_than_water