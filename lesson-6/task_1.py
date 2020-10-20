from time import sleep

class Trafficlight:
    __color = ['Красный', 'Желтый', 'Зеленый', 'Желтый', 'Красный']

    def running(self):
        i = 0
        while i != 5:
            print(Trafficlight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(7)
            elif i == 3:
                sleep(2)
            elif i == 4:
                sleep(7)
            i += 1

t = Trafficlight()
t.running()