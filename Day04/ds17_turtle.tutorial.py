from turtle import *
setup(width = 600, height = 600)

color('red', 'blue')
begin_fill()
while True:
    forward(100)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
