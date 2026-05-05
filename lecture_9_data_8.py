import matplotlib.pyplot as plt

# 1. 데이터 준비
cat = plt.imread('cat1.jpg')
dog = plt.imread('dog1.jpg')
imgs = [cat, dog]
labels = ['cat', 'dog']

# 2. 그래프 생성 설정
plt.figure(figsize=(5,3))

# 3. 반복문을 통한 이미지 및 라벨 출력
for i in range(len(imgs)):
    plt.subplot(1, 2, i+1) # 1행 2열 중 i+1번째 칸 선택
    plt.imshow(imgs[i])    # 이미지 표시
    plt.xticks([])         # x축 눈금 제거
    plt.yticks([])         # y축 눈금 제거
    plt.xlabel(labels[i])  # x축 하단에 라벨(이름) 표시

# 4. 화면 출력
plt.show()