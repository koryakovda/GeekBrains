import time
class TrafficLight:
    color = 'Red'

    def running(self,color):
        
        a = time.time()
        print('a=',a)
        if color == 'Green':
            print('Green')
            b = time.time()
            print('b=',b)
            while (b - a) > 7:

                print('Green')
                print('b-a=',b-a)
            else:
                a = time.time()
                color == 'Yellow'
        elif color == 'Yellow':
            print('Yellow')
            b = time.time()
            while b - a > 3:
                print(color)
            else:
                a = time.time()
                color == 'Red'
        elif color == 'Red':
            print('Red')
            b = time.time()
            a = time.time()
            while b - a > 5:
                print('Red')
                b = time.time()
            else:
                a = time.time()
                color == 'Green'


light = TrafficLight()
light.running('Green')
# print(light._color)