import matplotlib.pyplot as plt

# 데이터 준비
year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
seoul = [12.1, 12, 12.2, 12.5, 13.4, 13.6, 13.6, 13, 12.9, 13.5, 13.2, 13.7, 13.2]
jeju = [15.6, 15.6, 15.7, 16.5, 16.2, 16.7, 17, 16.8, 16.6, 16.8, 16.7, 17.5, 17]

# 그래프 크기 설정
plt.figure(figsize=(5,3))

#서울 데이터를 선 그래프로 그리기
plt.plot(year, seoul, label='seoul')

#서울 데이터를 선 그래프
plt.plot(year, jeju, label='jeju')

#y축의 범위를 제한
plt.ylim(10, 20)

#그래프 제목
plt.title('temperature')

#x축 하단
plt.xlabel('year')

#함수에 lable을 박스 형태로 표시
plt.legend()

#그래프 그리기
plt.show()