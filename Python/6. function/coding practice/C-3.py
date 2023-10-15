def member_join(*args) :
    result = ""
    for arg in args :
        result = result + arg + " "

    print('가입 회원 :' , result)

member_join('김정연' , '안서영')
member_join('황선형' , '김철영' , '이창연')
member_join('김정연' , '안서영' , '정수연' , '함소영')