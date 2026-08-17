    def box(func):
        def wrapper(*args,**kwargs):
            print("================================")
            result = func(*args,**kwargs)
            print("================================")
            return result
        return wrapper

        
        
        

    class Member:
        def __init__(self, user_id, password):
            self.user_id = user_id
            self.password = password  
            self.book_cnt = 0              # 이게 음수가 될일이 있을까 ? 음수가 됫을때의 에러 방어용 try / except만들기
            self.borrow_recode = []         #딱히 음수가 되도 에러가 날거같진 않긴 한데
                                            #도서 대출 / 반납 이력

    class Book:
        def __init__(self, title, author, genre):
            self.title = title
            self.author = author
            self.genre = genre 
            self.who_borrow_this = None
            Admin.book_db.append(self)





    #################################################################################################################
    ## 메인 화면에 있어야 할 정보
    # 1. 로그인
    # 2. 회원가입               # Admin의 self.current_user = None일때의 간소한 화면표기

    # if self.current_user != None 일때의 메인화면 표시

    # 1.도서 대출           (만듬)
    # 2.대출 이력 열람      (만듬)
    # 3.로그아웃 ?  구현 자체는 그리 어렵지 않을듯? 그냥 self.current_user를 None으로만 변경하면 되서 ?
    # 4.(일단은 4번. 로그아웃이 제일 마지막 번호임) 책 검색         (만듬)
    # 5. 도서 반납 (책은 최대 세권까지만 빌릴수 있게 cnt를 만들어두자. 별로 의미는 없긴 헌디)       (만듬)

    class Admin: 
        user_db = {}       # db들은 추후에 수정.(다른 파일과 연동시키기)
        book_db  = []
        def __init__(self): 
            self.current_user = None  # 현재 이 프로그램에 접속해서 프로그램을 움직이는 Member 객체의 아이디
            self.character = None

        def show_book_detail(self, book):               # 책 상세정보
            print(f"제목 : {book.title}")
            print(f"작가 : {book.author}")
            print(f"장르 : {book.genre}")
            if book.who_borrow_this == None:
                print("현재 대출 가능한 도서입니다")
            else:
                print(f"{book.who_borrow_this.user_id}님이 대출중이에요.")
                return

        def book_index_borrow(self, sta_num, end_num):
            n = 0
            temp = {}
            for title in Admin.book_db[sta_num : end_num]:
                n += 1
                print(f"{n} : {title.title}")
                temp[n] = title
            return temp

        def return_book(self):
            n = 0
            temp = {}
            for book in Admin.book_db:
                if book.who_borrow_this == self.current_user:
                    n += 1
                    print(f"{n} : {book.title}")
                    temp[n] = book
            return temp

        def book_recode(self):
            print("도서 기록은 최근 20건까지만 표시됩니다.")
            for recode in self.current_user.borrow_recode[-20:]:
                print(recode)
            return
                    


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
                        continue
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

        @box
        def borrow_book(self):
            sta_num = 0             # 인덱스의 나침반역할
            end_num = 10
            while True:
                try:
                    temp = self.book_index_borrow(sta_num, end_num)
                    print("알맞은 명령어를 입력해주세요")
                    user_input = input("1~10 : 책 상세정보, 이전 : 이전 페이지 다음 : 다음 페이지, 0 : 이전 화면")
                    if user_input == '0':
                        break
                    elif user_input == "다음":
                        if end_num >= len(Admin.book_db):
                            print("다음 페이지가 존재하지 않습니다")
                            continue
                        sta_num += 10
                        end_num += 10
                        continue
                    elif user_input == "이전":
                        if sta_num - 10 < 0:
                            print("이전 페이지가 존재하지 않습니다")
                            continue
                        else:
                            sta_num -= 10
                            end_num -= 10
                            continue
                    elif 1 <= int(user_input) <= 10:
                        if int(user_input) not in temp:
                            print("존재하지 않는 항목입니다")
                            continue
                        book = temp[int(user_input)]
                        self.show_book_detail(book)     #만들어 둿던 함수 재탕
                        if book.who_borrow_this is not None:    # 만들어 둿던 코드 재탕후 조금 수정
                            print("책 목차  메인 화면으로 되돌아갑니다")
                            continue           # 이전화면으로 돌아가기 (초기 검색 화면)
                        borrow_input = input("1: 대출 , 2: 이전화면")
                        if not 1 <= int(borrow_input) <= 2:
                            raise ValueError
                        elif borrow_input == '1':
                            if self.current_user.book_cnt >= 3:
                                print("빌린 책을 반납 후 책 대출을 진행해주세요.")
                                break
                            else:
                                print("정상적으로 대출 되었습니다.")
                                self.current_user.book_cnt += 1
                                book.who_borrow_this = self.current_user
                                self.current_user.borrow_recode.append(f"{book.title} 대출")
                                break
                    else:
                        raise ValueError
                except ValueError:
                    print("정확한 숫자 혹은 문자를 입력해주세요.")
                    continue



        @box
        def search(self):
                n = 1
                temp = {}
                print("책 검색")
                user_input = input("찾으시는 책을 검색 해주세요:")
                for title in self.book_db:
                    if user_input in title.title:
                        print(f"{n} : {title.title}")
                        temp[n] = title 
                        n += 1
                if n == 1:
                    print("관련 책을 찾을 수 없어요. 다시 검색해주세요.")
                else: 
                    print("목차를 입력 혹은 0(뒤로 가기)을 입력해주세요.")
                    user_input_2 = input("목차 혹은 0 을 입력해주세요.")
                    try:
                        if user_input_2 == '0':
                            return self.search()
                        elif 1 <= int(user_input_2) < n:         #딕셔너리에서 n에 해당하는 타이틀의 상세정보를 book_db에서 찾아내어 양식에 맞게 출력
                            book = temp[int(user_input_2)]
                            self.show_book_detail(book)
                            if book.who_borrow_this is not None:
                                print("책 검색 메인 화면으로 되돌아갑니다")
                                return self.search()            # 이전화면으로 돌아가기 (초기 검색 화면)
                            borrow_input = input("1: 대출 , 2: 이전화면")
                            if not 1 <= int(borrow_input) <= 2:
                                raise ValueError
                            elif borrow_input == '1':
                                if self.current_user.book_cnt >= 3:
                                    print("빌린 책을 반납 후 책 대출을 진행해주세요.")
                                    return
                                else:
                                    print("정상적으로 대출 되었습니다.")
                                    self.current_user.book_cnt += 1
                                    book.who_borrow_this = self.current_user
                                    self.current_user.borrow_recode.append(f"{book.title} 대출")
                            return
                        else:
                            return 
                    except ValueError:
                        print("정확한 숫자를 입력해주세요.")
                        return self.search()
                return
                    


        def book_return(self):
            # 말 그대로 책을 반납.
            # 책 제한 3권은 위쪽에 책 대여 함수에서 처리하는편이 좋을듯? 아 member별로 따로 cnt를 만들어놓자.
            # 반납 화면은 저기 위에 만들어놓을 리스트 재탕.
            # who_borrow_this = self.user_id 인 도서목록 리스트에 올림.
            # 반납 후 who_borrow_this = None, Member.book_cnt -= 1 로 수정하기  #만약 어떤 오류로 인해 cnt 0인 유저가 -1이 되지않도록 
            ##except cnt < 0:  cnt = 0 이라고 해놓자
            #어차피 최대 세권이니깐 함수 쓸거 없이 그냥 표기하는게 나을거같은데 ? 
            while True:
                try:
                    temp = self.return_book()
                    user_input = input("1~3: 부분 반납, 4 : 전체 반납, 0 : 이전 화면")
                    if not user_input.isdigit():
                        raise ValueError
                    elif 1 <= int(user_input) <= 3:
                        if int(user_input) not in temp:
                            print("존재하지 않는 인덱스 입니다.")
                            continue
                        else:
                            book = temp[int(user_input)]
                            if self.current_user.book_cnt == 0:
                                print("대여중인 책이 존재하지 않습니다.") #여기까지 올일이 없긴 하지만 무슨 버그가 터질지 모르니깐.
                                break
                            book.who_borrow_this = None
                            self.current_user.book_cnt -= 1
                            self.current_user.borrow_recode.append(f"{book.title} 반납")
                            print(f"{book.title}을 반납하셧습니다.")
                            continue
                    elif user_input == "4":
                        print("모든 책을 반납합니다.")
                        for book in temp.values():
                            print(f"{book.title}을 반납하셧습니다.")
                            self.current_user.book_cnt -= 1
                            self.current_user.borrow_recode.append(f"{book.title} 반납")
                            book.who_borrow_this = None
                        print("메인 화면으로 이동합니다.")
                        break
                    elif user_input == '0':
                        print("메인 화면으로 이동합니다.")
                        break
                except ValueError:
                    print("정확한 숫자를 입력해주세요.")
                    continue
        @box
        def user_recode(self):
            self.book_recode()
            return

        @box
        def logout(self):
            self.current_user = None
            print("방문해주셔서 감사합니다")
            print("좋은 하루 되세요")
            return


        