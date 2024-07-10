from turtle import *

user_size:int = int(input("Choose size for fractal: "))
user_level:int = int(input("Choose amount of levels for fractal:"))
user_angle:int = int(input("Choose angle for fractal: "))
user_speed:int = int(input("Choose speed for fractal to be drawn: "))
shape("turtle")
speed(user_speed)

def fractal(size:int, level:int, angle:int):
    if level == 0:
        return
    
    forward(size)
    right(angle)
    fractal(size * 0.95, level -1, angle)

    left(angle * 2)

    fractal(size * 0.95, level -1, angle)

    right(angle)
    backward(size)
 

fractal(user_size,user_level,user_angle)
mainloop()