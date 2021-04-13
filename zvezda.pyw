import turtle, time
m = 20
n = 3
turtle.speed(10)
for i in range(m):
    turtle.color("red")
    for j in range(n):
        turtle.forward(60)
        turtle.left(120)
    turtle.color("black")
    turtle.forward(10)
    turtle.left(18)
time.sleep(5)
