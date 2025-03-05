import turtle as tr
def isaret(): 
	for i in range(200): 
		tr.right(1) 
		tr.forward(1) 
for i in range(1,6):
	def kalp(): 
		tr.fillcolor('red') 
		tr.begin_fill() 
		tr.left(140) 
		tr.forward(113) 
		isaret() 
		tr.left(120) 
		isaret() 
		tr.forward(112) 
		tr.end_fill() 
def yazi(): 
	tr.up() 
	tr.setpos(-68, 95) 
	tr.down() 
	tr.color('Black') 
	tr.write("Hayırlı Cumalar ❤", font=( 
	"Verdana", 12, "bold")) 
kalp() 
yazi() 
tr.ht() 
tr.mainloop()