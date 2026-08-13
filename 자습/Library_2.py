class Book:
    def __init__(self, title,book_id):
        self.title = title
        




class Library:
    id_pw_db = {}
    def __init__(self, id, pw):         #회원가입 할때 생성될 객체들 ?
        self.id = id
        self.pw = pw
        id_pw_db += self.id, self.pw

    def libra(self):
        while True:
            

