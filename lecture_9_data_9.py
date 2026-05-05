import matplotlib.pyplot as plt
import os

# 1. 'catdog' 폴더 내의 모든 파일 목록 가져오기
imgs = os.listdir('catdog')

# 2. 그래프 창 크기 설정 (5x5 인치)
plt.figure(figsize=(5,5))

# 3. 파일 목록의 개수만큼 반복 실행
for i in range(len(imgs)):
    # 3x3 격자 중 (i+1)번째 칸 선택
    plt.subplot(3, 3, i+1)
    
    # 폴더 경로와 파일 이름을 합쳐서 이미지 읽어오기
    img = plt.imread(os.path.join('catdog', imgs[i]))
    
    # 이미지 출력 및 축 눈금 숨기기
    plt.imshow(img)
    plt.axis('off')

# 4. 전체 결과 화면에 표시
plt.show()