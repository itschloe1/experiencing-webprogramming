#1. 리스트나 튜플에서 임의로 하나의 값을 뽑으려면?
import random
#리스트 데이터 생성
list1 = [1,2,3,4,5]
#튜플 데이터 생성
tuple1 = (1,2,3,4,5)

#리스트와 튜플 형태의 데이터에서 랜덤 뽑기
result = {"list_random": random.choice(list1),
          "tuple_random": random.choice(tuple1)
         }
import collections
result_1 = collections.OrderedDict(result)
#   print(result_1)
print(result_1)
# #또는 random.randint를 이용
# list_random2 = random.randint(1,5)
