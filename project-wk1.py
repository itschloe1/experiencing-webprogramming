# 구현 내용
#
# 처음 파이썬 파일을 실행 시키면, 한식, 중식, 일식 중 한 가지를 고르라는 내용이 나옵니다.
# 그 중에서 한 가지를 고르면 식당 이름을 하나 임의로 추천해 줍니다.
# 힌트
#
# 리스트를 여러 개 사용하고 사용자의 입력을 받아야 합니다
import random
koreanmenu = ["된장찌개", "김치찌개"]
chinesemenu = ["짜장면", "짬뽕", "탕수육"]
japanesemenu = ["스시", "초밥", "규카츠"]
choice = int(input("다음 메뉴 중 한 가지를 고르세요. 1.한식, 2.중식, 3.일식"))
def pickurchoice(choice):
    if choice == 1:
        return random.choice(koreanmenu)
    elif choice == 2:
        return random.choice(chinesemenu)
    else:
        return random.choice(japanesemenu)
print(pickurchoice(choice))
