class Member:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password        






#################################################################################################################
### Admin을 만들어 보자.......뭐부터 해야하지? 
### 어드민에 들어가야 할 기본적인 정보들.
### 유저 데이터 (id,pw)
### 책 데이터 (책 제목,작가,장르,대출 여부(더 나아갈수 있다면 누가 빌렷는지 까지))
### 책 데이터에서 더 나아가서 기한까지 설정할수 있다면 좋겟지만. 그러면 너무 복잡해질거 같다.
### 우선은 이정도. 필요한게 있다면 그때가서 추가하고 조정해보자.

class Admin: 
    def __init__(self): 
        self.user_db = {}       # db들은 추후에 수정.(다른 파일과 연동시키기)
        self.book_db  = []
        self.current_user = None  # 현재 이 프로그램에 접속해서 프로그램을 움직이는 Member 객체의 아이디



    def register(self):
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
    def login(self):
            print("================================")
            print("   도서 대출  &  대여 시스템      ")
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
################################################################################################

class Book:
    def __init__(self, title, author, genre):
         self.title = title
         self.author = author
         self.genre = genre 
         self.who_borrow_this = None       #일단 이 변수는 당장 비었으니까 이런식으로 처리를 해두는게 좋을까.
         self.character = None             #추후에 확장성을 고려.우선 만들어는 두자.
                                           #Book class 에 필요한 함수가 뭐가 있을까 ..? 흠 
                                           