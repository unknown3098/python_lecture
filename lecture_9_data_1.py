import matplotlib.pyplot as plt
year = {2014, 2015, 2016, 2017, 2018, 2019, 2020}
gdp = {3079.9, 3250.1, 3398.8, 3574, 3578.2, 3721.8, 3744, 4003.6, 4165.5}

#x,y 그래프 그리기
plt.plot(year, gdp)


#그래프의 크기
plt.figure(figsize=(5,3))

#데이터를 기반으로 선 그래프
plt.plot(year, gdp, 'g.-')

#그래프 제목
plt.title('GDP per capita')

#X축 하단
plt.xlabel('years')

#y축 상단
plt.ylabel('ten thousand won')

#Y축의 범위를 제한
plt.ylim(2500, 4500)

#그래프 출력
plt.show()