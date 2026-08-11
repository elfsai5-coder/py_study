import random
cnt = 0
n = random.randint(1,100)
while True:
    try:
        answer = int(input("1부터 100까지의 숫자를 입력해주세요~\n"))
        if answer < n:
            print("그거보단 커요")
        elif answer > n:
            print("그거보단 작아요")
        else:
            print(f"정답! {cnt}번만에 맞추셧어요~")
            break
    except ValueError:
            print("숫자만 적어주세요~")
    cnt += 1