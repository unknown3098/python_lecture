import matplotlib.pyplot as plt

# 데이터 준비
name = ['Jessica', 'Liam', 'Sophia']
x = [75, 92, 83]
y = [79, 89, 90]

# 그래프 생성
plt.figure(figsize=(5,3))

# 산점도 그리기
plt.scatter(x, y)

# 각 점에 주석 추가
plt.annotate(name[0], (x[0], y[0]), xytext=(5, -10), textcoords='offset points')
plt.annotate(name[1], (x[1], y[1]), xytext=(5, -10), textcoords='offset points')
plt.annotate(name[2], (x[2], y[2]), xytext=(5, -10), textcoords='offset points')

# 축 범위 및 라벨 설정
plt.xlim(73, 95)
plt.ylim(75, 93)
plt.xlabel('X')
plt.ylabel('Y')

plt.show()