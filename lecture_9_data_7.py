import matplotlib.pyplot as plt

# 1. 이미지 읽어오기
cat = plt.imread('cat1.jpg')

# 2. 이미지 표시 설정
plt.figure(figsize=(3,3))
plt.imshow(cat)
plt.axis('off')

# 3. 결과 저장 및 출력
plt.savefig('result.png')
plt.show()