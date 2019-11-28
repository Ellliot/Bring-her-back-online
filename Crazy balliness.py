from tkinter import *
from supercollider import Server, Synth
from tkinter import messagebox
import random
import time
class Ball:
    def __init__(self, canvas, paddle, color, list1):
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
        self.list = list1
        self.count = 0
        self.bg = "white"
        self.chart = [ "red", "blue", "purple", "yellow", "green", "HotPink1", "white"]

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3] or pos[1] <= paddle_pos[3] and pos[1] >= paddle_pos[1] :
                return True
            return False
        
    def changeColor(self):
        self.color = random.choice(self.chart)
        canvas.itemconfigure(self.id, fill=self.color)
    def bgChangeColor(self):
        self.bg = random.choice(self.chart)
        self.canvas.configure(bg=self.bg)
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        name = str(random.randrange(1,8))
        if(self.count == 1):
            self.bgChangeColor()
            self.count = 0
        '''if len(self.list) != 0:
            synth = random.choice(self.list)
            oldFreq = synth.get("freq")
            oldBwr = synth.get("bwr")
            if self.y < 0:
                if oldFreq <= 1000:
                    synth.set("freq", oldFreq + 5)
            else:
                if oldFreq >= 500:
                    synth.set("freq", oldFreq - 5)
            if self.x < 0:
                if oldBwr <= 1:
                    synth.set("bwr", oldBwr + 0.01)
            else:
                if oldBwr >= 0:
                    synth.set("bwr", oldBwr - 0.01)'''
                
        if pos[1] <= 0:
            self.y = 3
            name = Synth(server, str(self.load_preset(name)), { "freq" : random.randrange(100,2000) , "bwr" : 0.05 })
            self.list.append(name)
        if pos[3] >= self.canvas_height:
            self.y = -3
        if self.hit_paddle(pos) == True:
            if self.y > 0:
                self.y = -3;
            else:
                self.y = 3
            self.hit_behave()
            self.count += 1
            if len(self.list) != 0:
                pick = random.choice(list1)
                self.list.remove(pick)
                pick.free()
            
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        self.canvas.after(1, self.draw)
    def load_preset(self,name):
        if self.bg == "red":
            return "event3"
        if self.bg == "green":
            return "bubbly"
        if self.bg == "yellow":
            return "atari2600"
        if self.bg == "yellow":
            return "sine"
        if self.bg == "blue":
            return "sine"
        if self.bg == "HotPink1":
            return "event3"
        if self.bg == "white":
            return "sine"
            
    def hit_behave(self):
        if self.color == "red":
            synth1 = Synth(server, "atari2600") #C4
        if self.color == "green":
            synth2 = Synth(server, "atari2600") #A4
        if self.color == "purple":
            synth2 = Synth(server, "atari2600") #G4
        if self.color == "yellow":
            synth2 = Synth(server, "atari2600") #D4
        if self.color == "blue":
            synth2 = Synth(server, "atari2600") #F4
        if self.color == "HotPink1":
            synth2 = Synth(server, "atari2600") #E4
        if self.color == "white":
            synth2 = Synth(server, "atari2600") #B4
  
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 200)
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
        self.canvas.after(1, self.draw)
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
paddle = Paddle(canvas, 'black')
list1 =[]
ball1 = Ball(canvas, paddle, 'yellow', list1)
ball1.draw()
paddle.draw()
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        tk.destroy()
        for i in range(len(list1)):
            list1[i].free();

tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.mainloop()

