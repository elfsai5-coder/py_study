import data

admin = data.Admin()

while True:
    try:
        if admin.current_user == None:
            print("=================================")
            print("      도서 대출 / 반납 시스템      ")
            print("1. 로그인                         ")
            print("                                 ")
            print("2. 회원 가입                      ")
            print("=================================")
            while True:
                user_input = input("1.로그인, 2.회원가입 원하시는 서비스에 해당하는 숫자를 입력해주세요.")
                if user_input == '2':
                    admin.register()
                elif user_input == '1':
                    admin.login()
                else:
                    raise ValueError
                if admin.current_user != None:
                    break
    except ValueError:
        print("원하시는 서비스에 해당하는 숫자를 입력해주세요.")
        continue

    else:
        # 도서 대출 , 도서 반납, 책 검색, 이력 열람 ,로그 아웃
        print("=================================")
        print(f"    환영합니다 {admin.current_user.user_id}님      ")
        print("")
        print("1.도서 대출")
        print("2.도서 반납")
        print("3.도서 검색")
        print("4.이력 조회")
        print("5.로그아웃")
        print("=================================")
        try:
            user_input = int(input("원하시는 서비스를 숫자로 선택해주세요."))
            if user_input == 1:
                admin.borrow_book()
            elif user_input == 2:
                admin.book_return()
            elif user_input == 3:
                admin.search()
            elif user_input == 4:
                admin.user_recode()
            elif user_input == 5:
                admin.logout()
            else:
                raise ValueError
        except ValueError:
            print("원하시는 서비스를 숫자로 선택해주세요.")
            continue
    
            