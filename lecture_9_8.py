import multiprocessing
import time

## 클래스 선언 부분 ##
class RacingCar :
    carName = ''
    def __init__(self, name) :
        self.carName = name

    def runCar(self) :
        for _ in range(0, 3) :
            carStr = self.carName + '~~ 달립니다.\n'
            print(carStr, end = '')
            time.sleep(0.1) # 0.1초 쉬기

## 메인 코드 부분 ##
if __name__ == "__main__" :
    # 1. 자동차 인스턴스 생성
    car1 = RacingCar('@자동차1')
    car2 = RacingCar('#자동차2')
    car3 = RacingCar('$자동차3')

    # 2. 프로세스 생성 (14~16행)
    # target에는 실행할 메서드나 함수를 지정합니다.
    mp1 = multiprocessing.Process(target = car1.runCar)
    mp2 = multiprocessing.Process(target = car2.runCar)
    mp3 = multiprocessing.Process(target = car3.runCar)

    # 3. 프로세스 시작 (18~20행)
    mp1.start()
    mp2.start()
    mp3.start()

    # 4. 프로세스 종료 대기 (22~24행)
    mp1.join()
    mp2.join()
    mp3.join()