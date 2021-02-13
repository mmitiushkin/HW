from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        for i in range(3):
            print(f'Color: {TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            if i == 1:
                sleep(2)
            if i == 2:
                sleep(4)


tf = TrafficLight()
print(tf.running())
