import turtle

tela = turtle.Screen()

pincel = turtle.Pen()
pincel.speed('fastest')
pincel.hideturtle()
pincel.begin_fill()
pincel.circle(2)
pincel.end_fill()

tela.exitonclick()