#숙제 2번 예시 
import random, time

num = [] 
while True: 
    i = input("로또 번호를 추출합니까?(y/n)")

    if i == "y" : 
      num = random.sample(range(1,46),6)
      num.sort() 
      print(num)
     
    else  : 
     print("로또 추출을 종료합니다.")    
