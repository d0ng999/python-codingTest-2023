# 프렉탈 원 그리기
import turtle # 그림 그려주는 거북이
turtle.setup(width = 600, height = 600)

t = turtle.Turtle() # 거북이 만들기
t.shape('turtle')

c = t.clone() # 거북이 복제
c.color('black')


for i in range(1, 10):
    if i % 2 != 0:
        c.circle(-(i+1)*10)
    else:
        c.circle(i*10)

turtle.mainloop()