Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Pen()
>>> tao.shape('turtle')
>>> for i in range(4):
	tao.forward(50)
	tao.left(90)

	
>>> tao.penup()
>>> tao.goto(-100,-100)
>>> tao.pendown()
>>> for i in range(4):
	tao.forward(50)
	tao.left(90)

	
>>> tao.penup()
>>> tao.goto(50,50)
>>> tao.goto(-50,-50)
>>> for i in range(4):
	tao.forward(50)
	tao.left(90)

	
>>> tao.pendown()
>>> for i in range(4):
	tao.forward(50)
	tao.left(90)

	
>>> tao.penup()
>>> tao.goto(50,-50)
>>>

