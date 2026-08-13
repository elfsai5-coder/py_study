class Library:
    ID_PW_DB = {}
    def __init__(self, id,pw):
        self.id = id
        self.pw = pw
        ID_PW_DB += {self.id : self.pw}

lww127 = Library("lww127", 97102100)

    def Libra(self):
        while True:
            print("=========================")
            print("|      환영합니다  !     |")
            print("| 1.로그인               |")
            print("| 2.책 검색              |")
            print("| 3.책 대여 / 반납       |")
            print("| 4.회원 가입            |")
            print("| 5.회원 도서 이력 열람   |")
            print("| 6.회원 정보 수정       |")
            print("| 7.도서 시스템 종료      |")
            print("=========================")
            print("해당하는 항목의 번호를 적어주세요 ~")
            try:
                user_input = int(input())
                if user_input < 0 or user_input > 7:
                    raise ValueError
                if user_input == 1:
                    print("=========================")
                    print("| ID와 PASSWORD 를       |")
                    print("|    입력 해주세요.      |")
                    print("=========================")
                    id_input = input("ID를 입력해주세요 ~")
                    global ID_PW_DB
                    if id_input in ID_PW_DB.keys():
                        pw_input = ("패스워드를 입력해주세요 ~ ")
                        if ID_PW_DB in {id_input : pw_input}:
                            print("=========================")
                            print(f"환영합니다 {id_input}님!")
                            print("=========================")
                        else:
                            print("비밀번호가 틀렷어요. 다시한번 확인해주세요.")
                    else:
                        print("존재하지 않는 아이디입니다.회원가입을 진행해주세요.")
            except ValueError:
                print("해당하는 항목의 번호만 적어주세요 ~")



# 위에 적어놓은거 싹다 갈아엎고 다시 해보기

# 가장 처음 로그인 창부터 구현
# 1.아이디 비밀번호 인풋 입력  창 2.회원가입 3.시스템 종료

# 그 이후 아무튼 로그인 완료된 이후.
# 1.도서 대여 / 반납 (주요 기능이니 1번)
# 2.도서 검색       (도서를 검색,db에 있는지 확인. llm이용.도서를 검색후 간단한 스토리를 알수 있도록.혹은 이와 비슷한 책을 찾을수있도록)
#                  (사용자의 자율성 제한. llm과의 대화는 선택지 식으로 제한(돈없음) 당장의 선택지 두개. 1. 비슷한 책 / 2.간략한 스토리 
# 3.도서 이력 열람   ( 객체별 도서 대여/반납 이력을 조회)
# 4



