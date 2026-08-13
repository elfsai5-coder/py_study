class Member:
    user_db = {}
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password

    @staticmethod
    def register():
        while True:
            print("================================")
            print("   사용하실 아이디와 패스워드를   ")
            print("          입력해주세요 ~         ")
            print("================================")
            id_input = input("사용하실 아이디를 입력해주세요: ")
            if id_input in Member.user_db:
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
                Member.user_db[id_input] =  Member(id_input, pw_input)
                return # 회원가입 완료      
                    #json 파일 만들어서 진짜 db로 교체하는거는 우선 나중에 하기 우선 뼈대부터 세우고 
    
    @staticmethod
    def login():
        print("================================")
        print("   도서 대출  &  대여 시스템      ")
        print("아이디와 비밀번호를 입력해주세요 ~ ")
        print("================================")
        id_input = input("아이디를 입력해주세요: ")
        if id_input in Member.user_db:
            print("================================")
            print("         비밀 번호를             ")
            print("        입력 해주세요 ~          ")
            print("================================")
            pw_input = input("비밀번호를 입력 해주세요: ")
            if pw_input == Member.user_db[id_input].password:
                print("================================")
                print(f" 환영 합니다 {id_input}님 ~      ")
                print("     좋은 하루 되세요 ~          ")
                print("================================")
                #지금 로그인한 유저가 어떤 객체인지 인식할수 있는 패턴 추가 필요

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


        


Member.register()
Member.login()