from tkinter import *
from supercollider import Server, Synth, Buffer
from tkinter import messagebox
import random
import time
import tkinter
from playsound import playsound
from threading import Thread

class Ball:
    def __init__(self, canvas, paddle, color,img, img2, img3, list1):
        self.canvas = canvas
        self.paddle = paddle
        self.color = color
        self.id = canvas.create_oval(10, 10, 25, 25, fill=self.color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.bg = "None"
        self.chart = ["white", "green", "blue2", "yellow", "HotPink1", "black", "Timara", "Timara2", "curtain", "curtain", "curtain", "curtain","end","realEnd"]
        self.name = Synth(server, "playbuf", {"bufnum":2, "loop" :0})
        self.flag = False
        self.count = 0
        self.img = img
        self.list = list1
        self.cycle = 0
        self.img2 = img2
        self.img3 = img3
        self.txt = ["Bring", "Her", "Back", "Online"]
        self.canvas.create_text(250,50, text ="Be Warned", font="Times 40 bold", fill = "red", tag = "w")
        self.canvas.create_text(250,210, text ="High frequency Noises\nFlashing lights\nUseless content\n", font="Times 40 bold", fill = "black", tag = "w")
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3] or pos[1] <= paddle_pos[3] and pos[1] >= paddle_pos[1] :
                return True
            return False
    def maintainCount(self):
        if self.cycle < 1:
            if self.count == 6:
                self.count = 0
                self.cycle+=1
        elif self.cycle == 1:
            if self.count == 7:
                self.count = 0
                self.cycle+=1
        elif self.cycle == 2:
            if self.count == 8:
                self.count = 0
                self.cycle+=1
                
    def changeColor(self):
        self.color = random.choice(self.chart)
        canvas.itemconfigure(self.id, fill=self.color)
    def bgChangeColor(self):
        self.bg = self.chart[self.count-1]
        if self.flag == True:
            self.canvas.delete("secret")
            self.flag = False
        if self.bg == "Timara":
            pic = canvas.create_image(10,10, anchor=NW, image=self.img, tag = "Timara")
            canvas.tag_lower(pic)
        elif self.bg == "Timara2":
            pic2 = canvas.create_image(0,10, anchor=NW, image=self.img2, tag = "Timara2")
            canvas.tag_lower(pic2)
            canvas.tag_lower("Timara")
        elif self.bg == "curtain":
            canvas.delete("Timara")
            canvas.delete("Timara2")
            canvas.delete("t")
        elif self.bg == "end":
            canvas.delete("y")
            self.canvas.configure(bg="white")
            for i in range(len(list1)):
                list1[i].free();
        elif self.bg == "realEnd":
            self.canvas.delete(self.id)
            self.name = Synth(server, "playbuf", {"bufnum":1, "loop" :0})
            show = self.canvas.create_text(250,200, text ="TECH 201 SHOWCASE", font="Times 40 bold", fill = "coral1", tag = "show")
            pic3 = canvas.create_image(0,10, anchor=NW, image=self.img3, tag = "Timara3")
            canvas.tag_lower(pic3)
        else:
            self.canvas.configure(bg=self.bg)
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if self.hit_paddle(pos) == True:
            if self.y > 0:
                self.y = -3;
            else:
                self.y = 3
            if self.cycle == 0:
                if self.bg != "black":
                    self.name.free()
            self.maintainCount()
            self.count +=1
            self.hit_behave()
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        self.change(pos)
        self.canvas.after(5, self.draw)
    def change(self, pos):
        synth = self.name
        if self.bg == "green":
            synth.set("freq", pos[2]*4) #x
            synth.set("bwr", pos[1]/400) #y
            if self.flag == False:
                self.canvas.create_text(random.randrange(10,490), random.randrange(10,390),fill="green",font="Times 40 bold", text="WHO", tag="t")
                self.canvas.create_text(250,190,fill="black",font="Times 20 bold", text="in the wilderness", tag="secret")
                self.flag = True
        if self.bg == "blue2":
            synth.set("freq", pos[2]/5)
            synth.set("decay", pos[1]/40)
            self.canvas.create_text(random.randrange(10,490), random.randrange(10,390), fill = "yellow",  font = "Times 30 bold", text = "BUBBLES", tag = "b")
                
        if self.bg == "yellow":
            synth.set("freq", pos[2]*3)
            synth.set("hifreq", pos[1]*4)
            if self.flag == False:
                self.canvas.delete("b")
                self.canvas.create_text(random.randrange(10,490), random.randrange(10,390),fill="blue2",font="Times 30 bold", text="IS", tag="t")
                self.canvas.create_text(250,190,fill="blue2",font="Times 20 bold", text="in a dream", tag="secret")
                self.flag = True
            
        if self.bg == "white" and self.flag == False:
            self.canvas.delete("w")
            self.canvas.create_text(random.randrange(10,490), random.randrange(10,390), fill = "white",  font = "Times 40 bold", text = "A SHEEP", tag = "t")
            self.flag = True
        if self.bg == "black" and self.flag == False:
            self.canvas.create_text(250,200,fill="white",font="Times 20 bold", text="in the darkness", tag="secret")
            self.canvas.create_text(random.randrange(10,490), random.randrange(10,390), fill = "black",  font = "Times 50 bold", text = "AM!", tag = "t")
            self.flag = True
        if self.bg == "HotPink1" and self.flag == False:
            self.canvas.create_text(random.randrange(10,490), random.randrange(10,390), fill = "HotPink1",  font = "Times 60 bold", text = "I", tag = "t")
            self.canvas.create_text(250,190,fill="yellow",font="Times 20 bold", text="in love", tag="secret")
            self.flag = True
        if self.bg == "curtain":
            if self.flag == False:
                i= self.count - 9
                word = self.txt[i]
                self.canvas.create_text(100+90*i, 200,fill="yellow",font="Times 20 bold", text=word, tag="y")
                #self.name.set("bufnum", 3)
                self.flag = True
        
            
    def hit_behave(self):
        self.bgChangeColor()
        if self.bg == "white":
            self.name = Synth(server, "playbuf", {"bufnum":0, "loop":1})
        if self.bg == "yellow":
            self.name = Synth(server, "sawPad", {"freq" : random.randrange(100,1000)})
        if self.bg == "blue2":
            self.name = Synth(server, "bubbly", { "freq" : random.randrange(100,1700)})
        if self.bg == "HotPink1":
            self.name = Synth(server, "atari2600", { "freq" : random.randrange(100,1700)})
        if self.bg == "green":
            self.name = Synth(server, "resonz", { "freq" : random.randrange(100,1700)})
        if self.bg == "Timara" or self.bg == "Timara2":
            self.name = Synth(server, "playbuf", {"bufnum":0, "loop":1})
        if self.bg == "curtain":
            self.name = Synth(server, "playbuf", {"bufnum":0, "loop":1})
        self.list.append(self.name)
  
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, -110, 200)
        self.x = 0
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        '''self.canvas.bind_all('<KeyPress-Up>', self.turn_up)
        self.canvas.bind_all('<KeyPress-Down>', self.turn_down)'''
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
        if pos[1] <= 0:
            self.y = 0
        elif pos[3] >= self.canvas_height:
            self.y = 0
        self.canvas.after(5, self.draw)
    def turn_left(self, evt):
        self.x = -2
    def turn_right(self, evt):
        self.x = 2
    def turn_up(self, evt):
        self.y = -2
    def turn_down(self, evt):
        self.y = 2
    
tk = Tk()
server = Server()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
img = tkinter.PhotoImage(file="ARP2600.png")
img2 = tkinter.PhotoImage(file="Timara.png")
img3 = tkinter.PhotoImage(file="Studio4.png")
img3 = img3.subsample(10)
img2 = img2.subsample(3)
list1 =[]
paddle = Paddle(canvas, 'black')
ball1 = Ball(canvas, paddle, 'yellow', img, img2, img3, list1)
ball1.draw()
paddle.draw()
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        for i in range(len(list1)):
            list1[i].free();
        tk.destroy()

tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.mainloop()

