def add(n,n_2):
    return n + n_2

def minus(n,n_2):
    return n - n_2

VERSION = "1.0.0"

if __name__ == '__main__': # 터미널에서 실행할때 파일을 파이썬 main파일로 한정 ? 
    print("모듈명:",__name__)

    result = add(10,20)
    print("결과:", result)