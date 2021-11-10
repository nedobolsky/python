import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        while True:
            for el in TrafficLight.__color:
                print(el)
                if el == 'red':
                    time.sleep(7)
                elif el == 'yellow':
                    time.sleep(2)
                else:
                    time.sleep(10)


traffic = TrafficLight()
traffic.running()
