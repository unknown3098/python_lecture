class Car:

    색상 = ""
    현재_속도 =0


    def upSpeed(self, 증가속도):
        self.현재_속도 += 증가속도

    def downSpeed(self, 감소속도):
        self.현재_속도 -= 감소속도

        def printMessage():
            print("시험 출력이다.")


myCar1 = Car()
myCar2 = Car()
myCar3 = Car()

myCar1.color = "빨강"
myCar1.speed =0
myCar2.color = "파란"
myCar2.speed =0
myCar3.color = "노랑"
myCar3.speed =0

myCar.upSpeed(30)
myCar2.downSpeed(60)

myCar = Car()
myCar3.color = "노랑"
myCar3.speed =0

myCar1.upSpeed(30)
print("자동차1의 색상은 %s이며, 햔재 속도는 %dm입니다." % (myCar1.color, myCar1.speed))

myCar1.upSpeed(60)
print("자동차2의 색상은 %s이며, 햔재 속도는 %dm입니다." % (myCar2.color, myCar2.speed))

myCar1.upSpeed(30)
print("자동차3의 색상은 %s이며, 햔재 속도는 %dm입니다." % (myCar3.color, myCar3.speed))



