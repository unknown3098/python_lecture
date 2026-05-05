import matplotlib.pyplot as plt

# 1. 혈액형 데이터를 저장할 딕셔너리 초기화
blood = {'A':0, 'B':0, 'O':0, 'AB':0}

# 2. 반복문을 통해 데이터 입력 받기
while True:
    s = input('혈액형(A, B, O, AB) 또는 종료: ')
    
    if s == '종료':
        break
    elif s in blood:
        blood[s] += 1
    else:
        print('잘못 입력했습니다.')

# 3. 그래프 생성 및 설정
plt.figure(figsize=(5,3))
plt.bar(blood.keys(), blood.values(), width=0.6)

plt.xlabel('blood type')
plt.ylabel('frequency')
plt.show()