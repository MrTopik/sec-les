import turtle as t
for steps in range(17000):
    for c in ('blue', 'red', 'green'):
        t.color(c)
        t.forward(steps)
        t.right(179)
t.hideturtle()
t.mainloop()