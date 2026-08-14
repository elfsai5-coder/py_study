class Member:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password  
        self.book_cnt = 0              # 이게 음수가 될일이 있을까 ? 음수가 됫을때의 에러 방어용 try / except만들기
        self.borrow_recode = []         #딱히 음수가 되도 에러가 날거같진 않긴 한데
                                        #도서 대출 / 반납 이력






#################################################################################################################
## 메인 화면에 있어야 할 정보
# 1. 로그인
# 2. 회원가입               # Admin의 self.current_user = None일때의 간소한 화면표기

# if self.current_user != None 일때의 메인화면 표시

# 1.도서 대출
# 2.대출 이력 열람
# 3.로그아웃 ?  구현 자체는 그리 어렵지 않을듯? 그냥 self.current_user를 None으로만 변경하면 되서 ?
# 4.(일단은 4번. 로그아웃이 제일 마지막 번호임) 책 검색
# 5. 도서 반납 (책은 최대 세권까지만 빌릴수 있게 cnt를 만들어두자. 별로 의미는 없긴 헌디)

class Admin: 
    def __init__(self): 
        self.user_db = {}       # db들은 추후에 수정.(다른 파일과 연동시키기)
        self.book_db  = []
        self.current_user = None  # 현재 이 프로그램에 접속해서 프로그램을 움직이는 Member 객체의 아이디
        self.character = None



    def register(self):          # 회원가입
            while True:
                print("================================")
                print("   사용하실 아이디와 패스워드를   ")
                print("          입력해주세요 ~         ")
                print("================================")
                id_input = input("사용하실 아이디를 입력해주세요: ")
                if id_input in self.user_db:
                    print("================================")
                    print("   이미 사용중인 아이디에요 ~     ")
                    print("   다른 아이디를 입력 해주세요 ~  ")
                    print("================================")
                    break
                else:
                    pw_input = input("사용하실 비밀번호를 입력해주세요: ")
                    print("================================")
                    print(f"   {id_input}님의 회원가입이     ")
                    print("         완료 되었어요 ~         ")
                    print("================================")
                    self.user_db[id_input] =  Member(id_input, pw_input)
                    return # 회원가입 완료      
                        #json 파일 만들어서 진짜 db로 교체하는거는 우선 나중에 하기 우선 뼈대부터 세우고
    def login(self):                # 로그인
            print("================================")
            print("        도서  대여  시스템       ")
            print("아이디와 비밀번호를 입력해주세요 ~ ")
            print("================================")
            id_input = input("아이디를 입력해주세요: ")
            if id_input in self.user_db:
                print("================================")
                print("         비밀 번호를             ")
                print("        입력 해주세요 ~          ")
                print("================================")
                pw_input = input("비밀번호를 입력 해주세요: ")
                if pw_input == self.user_db[id_input].password:
                    print("================================")
                    print(f" 환영 합니다 {id_input}님 ~      ")
                    print("     좋은 하루 되세요 ~          ")
                    print("================================")
                    #지금 로그인한 유저가 어떤 객체인지 인식할수 있는 패턴 추가 필요 (완료?)
                    self.current_user = self.user_db[id_input]      # 로그인 이후 유저는 self.current_user 로 정의
                    return
    
                else:
                    print("================================")
                    print("      잘못된 비밀번호에요 ~       ")
                    print(" 비밀번호를 다시한번 확인 해주세요 ")
                    print("================================")
                    return 
    
            else:
                print("================================")
                print("   존재하지 않는 아이디에요 ~     ")
                print("     회원 가입을 진행해주세요     ")
                print("================================")
                return 


    def borrow_book(self):
         # 인덱스 형식으로 한 페이지에 10개씩 짤라서 표기. 대충 인풋으로 (1 : 다음, 2 : 이전 3 : 뒤로가기)를 적어서 페이지를 넘길수 있게
         # 마지막 페이지, 처음페이지 조건문으로 처리.
         # book_db에 book객체들의 정보를 저장.json파일에서 book의 who_borrow_this가 None이면 대출 가능한 책.으로 인지할수 있게 해야함
         # 1~10번까지의 번호를 인풋으로 입력하면 그 책의 자세한 정보를 표기할수 있도록? (1.대출 2.뒤로가기)
         # (1 : 대출 2 : 뒤로가기 ) 책을 빌릴때 Member객체의 borrow_recode에 책의 title과 분류(대출)을 기록해야함.
         # Member의 대출 이력을 보여주는 페이지는 여기서 만들 표기를 그대로 복붙해도 작동할듯 ? 
         # 책을 한권 빌리면 메인 화면으로 return (Member.book_cnt += 1)
         # 만약 member.book_cnt >= 3일경우 책 대여 불가 안내문 (반납부터하세요)

    
    def 책검색(self):
         # 책 검색
         # 인풋이 일부만 포함해도 검색내용에 뜨도록.
         # 사서의 도움 받기 << 만드는거도 ㄱㅊ할듯 ? llm연동해서    (책 추천)(db에 있는 책만 말해야됨)
         # 검색 후 (1.상세 정보 2.대출 )
         # (1.상세정보) 진입 후 책 대여에서 썻던 상세정보 양식 그대로 재탕(1.대출 2.뒤로가기)
         # 2.대출 진입시 대출 됫다는 안내문과 함께 메인화면 return

    def 책반납(self):
        # 말 그대로 책을 반납.
        # 책 제한 3권은 위쪽에 책 대여 함수에서 처리하는편이 좋을듯? 아 member별로 따로 cnt를 만들어놓자.
        # 반납 화면은 저기 위에 만들어놓을 리스트 재탕.
        # who_borrow_this = self.user_id 인 도서목록 리스트에 올림.
        # 반납 후 who_borrow_this = None, Member.book_cnt -= 1 로 수정하기  #만약 어떤 오류로 인해 cnt 0인 유저가 -1이 되지않도록 
                                                                #except cnt < 0:  cnt = 0 이라고 해놓자,
         

################################################################################################

class Book:
    def __init__(self, title, author, genre):
         self.title = title
         self.author = author
         self.genre = genre 
         self.who_borrow_this = None