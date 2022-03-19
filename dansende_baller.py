from tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 600

tk=Tk()
canvas=Canvas(tk,width=WIDTH,height=HEIGHT)
tk.title("Glade baller !")
canvas.pack()

class Ball:
    def __init__(self,color,size):
        self.shape = canvas.create_oval(10,10,size,size, fill=color)
        self.x_speed = random.randrange(1,20)
        self.y_speed = random.randrange(1,20)

    def move(self):
        canvas.move(self.shape,self.x_speed,self.y_speed)
        pos = canvas.coords(self.shape)
        if pos[3]>= HEIGHT or pos[1]<=0:
            self.y_speed=-self.y_speed
        if pos[2]>= WIDTH or pos[0] <=0:
            self.x_speed=-self.x_speed        
           

if __name__ == "__main__":
    #newball=Ball(20,"pink")
    #newball2=Ball(30,"forestgreen")
    colors=["cyan","orange","blue","green","dodgerblue","grey","red","pink","gold","silver","black","purple","turquoise","yellow","magenta","limegreen","violet"]    
    balls =[]
    for i in range(100):
        balls.append(Ball(random.choice(colors),random.randrange(50,100)))
    
    while True:
        for ball in balls:
            ball.move()
        tk.update()
        time.sleep(0.01)

tk.mainloop()







    
