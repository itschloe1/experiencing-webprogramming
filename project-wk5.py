def multiplication_dan():
    try:
        dan = int(input("몇 단을 출력 하시겠습니까?"))
        if (dan<2 or dan>9):
            print("2에서 9사이의 숫자만 입력해주세요")
            multiplication_dan()
        else :
            return dan
    except ValueError:
        print("숫자가 아닙니다.")

def multiplication_rslt(dan):
    for num in range(1, 10):
        print("{} * {} = {}".format(dan, num, dan * num))

dan = multiplication_dan()
multiplication_rslt(dan)
