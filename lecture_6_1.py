'''def get sum(n):
  sum = 0
for x in range(n):
  sum = sum + x + 1
return sum

print(get_sum(10))
print(get_sum(100))
print(get_sum(1000))''

print(abs(3.23))
print(ads(-3.23))

print(len("혼공프"))
print(len([1,2]))
print(len({"이름": "혼공프", "사용언어": "파이썬", "대상독자: "입문자"}))

def get_shop_name():
  return "커피장인"

def get_branch_name():
  return "여의도 본점"

def print_names():
  print(get_shop_name())
  print(get_branch_name())

print_names()

numbers = [0]

numbers.append(1)
print(numbers)

numbers.append(2)
print(numbers)

numbers.append(3)
print(numbers)

--------------------
order detail = []

def make_order(name, qty):
  order_detail.append({"이름": name, "수량" : qty})

print(order_detail)
make_order("아메리카노", 2)
make_order("플랫 화이트", 1)
print(order_detail)

-----------------------------


coffee = 0

coffee = int(input("어떤 커피를 드릴까요?(1:보통, 2:설탕, 3:블랙)))

print()
print("#1. 뜨거운 물을 준비한다.");
print("#2. 종이컵을 준비한다.");

if coffee == 1;
  print("#3, 보통커피를 탄다.")
elif coffee == 2:
  print("#3, 설탕커피를 탄다.")
elif coffee == 3:
  print("#3, 블랙커피를 탄다.")
else:
  print("#3, 아무거나 탄다.")

  ------------------------------

coffee = 0

def coffee_machine(button):

coffee = int(input("A손님, 어떤 커피를 드릴까요?(1:보통, 2:설탕, 3:블랙)))
coffe_machine(coffee)
print("A손님~ 커피 여기 있습니다.")

coffee = int(input("B손님, 어떤 커피를 드릴까요?(1:보통, 2:설탕, 3:블랙)))
coffe_machine(coffee)
print("B손님~ 커피 여기 있습니다.")

coffee = int(input("C손님, 어떤 커피를 드릴까요?(1:보통, 2:설탕, 3:블랙)))
coffe_machine(coffee)
print("C손님~ 커피 여기 있습니다.")

-----------------------


def calc(v1, v2, op) :
  result = 0
    if op == '+' :
        result = v1 + v2
    elif op == '-' :
        result = v1 - v2
    elif op == '*' :
        result = v1 * v2
    elif op == '/' :
        result = v1 / v2
        
    return result

## 전역 변수 선언 부분 ##
res = 0
var1, var2, oper = 0, 0, ""

## 메인 코드 부분 ##
oper = input("계산을 입력하세요(+, -, *, /) : ")
var1 = int(input("첫 번째 수를 입력하세요 : "))
var2 = int(input("두 번째 수를 입력하세요 : "))

res = calc(var1, var2, oper)

print("## 계산기 : %d %s %d = %d" % (var1, oper, var2, res))