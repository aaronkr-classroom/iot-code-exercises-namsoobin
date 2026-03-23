# 3_tuple.py
# RGB색상을 표현하는 튜플 예제
black = (0, 0, 0)
white = (255, 255, 255) # 8bit=1byte, 2^8bit=8byte
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
my_color = (24, 75, 189) #blue + purple

#my_color[2] =0 //값 변경 안됨. 재정의 해야함.
my_color = (24, 75, 0)

my_colors = [
    black, white, red,
    green, blue, my_color
    ]

for color in my_colors:
    print(color)