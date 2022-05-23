def plus(a,b):
    result = a+b
    return result 

while(True):  
    num1,num2 = map(int,input("연산을 진행할 두 숫자를 입력하시오. : ").split())
    i = input("어떠한 연산을 수행할까요?")
    
    if i=="+" :
        print(num1+num2)
    elif i=="-" :
        print(num1-num2)
    elif i=="*" :
        print(num1*num2)
    elif i=="/" :
        print(num1/num2)        

    else: 
        print("해당연산은 지원하지 않습니다. ")  