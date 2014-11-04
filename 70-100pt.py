#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")
enemy = drawpad.create_rectangle(0,280,110,300, fill="blue")
enemy1 = drawpad.create_rectangle(0,140,55,150, fill="red")
# Create your "enemies" here, before the class

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "green")
       	    self.down.grid(row=2,column=1)
       	    # Bind an event to the first button
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "green")
       	    self.right.grid(row=1,column=2)
       	    # Bind an event to the first button
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "green")
       	    self.left.grid(row=1,column=0)
       	    # Bind an event to the first button
       	    self.left.bind("<Button-1>", self.leftClicked)
       	   
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
            self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    global enemy
	    global enemy1
	    x1, y1, x2, y2 = drawpad.coords(enemy)
	    a1, b1, a2, b2 = drawpad.coords(enemy1)
	    if x1 >= drawpad.winfo_width():
	        drawpad.move(enemy,-drawpad.winfo_width(),0)
	    elif x2 < 0:
	        drawpad.move(enemy, 20, 0)
	    if a1 >= drawpad.winfo_width():
	        drawpad.move(enemy1,-drawpad.winfo_width(),0)
	    elif a2 < 0:
	        drawpad.move(enemy1, 20, 0)
	    drawpad.move(enemy,10,0)
	    drawpad.move(enemy1,20,0)
	    drawpad.after(1,self.animate)
	    # Remember to include your "enemies" with "global"
	
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
		
app = MyApp(root)
root.mainloop()