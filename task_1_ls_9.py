import time


class TrafficLight:

    def running(self):
        while True:
            self.__color = "Red"
            print(f'\033[41m{self.__color} ')
            time.sleep(7)
            self.__color = "Yellow"
            print(f'\033[43m{self.__color}')
            time.sleep(2)
            self.__color = "Green"
            print(f'\033[42m{self.__color}')
            time.sleep(7)


traffic = TrafficLight()
traffic.running()



