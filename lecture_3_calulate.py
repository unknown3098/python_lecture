base = int(input("입력 진수 결정(16/10/8/2) : "))
num_str = input("값 입력 : ")


dec_value = int(num_str, base)

print(f"16진수 ==> {hex(dec_value)}")
print(f"10진수 ==> {dec_value}")
print(f"8진수 ==> {oct(dec_value)}")
print(f"2진수 ==> {bin(dec_value)}")