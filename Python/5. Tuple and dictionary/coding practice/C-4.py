words = {'꽃' : 'flower' , '나비' : 'butterfly' , '학교' : 'school' , '자동차' : 'car' , '비행기' : 'airplane' ,}

print('<영어 단어 맞추기 퀴즈>')

for kor in words:
    input_words = input('%s에 해당되는 영어 단어를 입력해주새요 :' % kor)

    if input_words == words[kor] :
        print('정답입니다!')
    else :
        print('틀렸습니다!')