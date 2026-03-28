select = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계 : "))

if select == 1:
    expression = input("*** 수식을 입력하세요 : ")
    answer = eval(expression)
    print(f"{expression} 결과는  {answer}입니다.")

elif select == 2:
    num1 = int(input("*** 첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("*** 두 번째 숫자를 입력하세요 : "))
    
    total = 0
    # num1부터 num2까지의 합계 계산
    for i in range(num1, num2 + 1):
        total += i
        
    print(f"{num1}+...+{num2}는 {total}입니다.")

else:
    print("1 또는 2를 정확히 입력해주세요.")