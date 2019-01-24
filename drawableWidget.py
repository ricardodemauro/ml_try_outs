import tkinter as tk
from PIL import Image, ImageDraw

class DrawableArea():
    
    def onMouseDown(self, event):
        if self.trace:
            print('mouse down')
            
        if self.drawing:
            self.drawing = False
        else:
            self.drawing = True
    
    def start(self):
        self.startPillow()
        
        self.canvas = tk.Canvas(root, width=self.width, height=self.height)
        self.canvas.pack()
        self.old_coords = None
        self.drawing = False
        self.root.bind('<Motion>', self.onDraw)
        self.root.bind('<Button-1>', self.onMouseDown)
        self.root.bind('<KeyPress>', self.onKeyDown)
    
    def startPillow(self):
        self.img = Image.new("RGB", (self.width, self.height), self.bg)
        self.draw = ImageDraw.Draw(self.img)

    def onDraw(self, event):
        x, y = event.x, event.y
        
        if self.old_coords and self.drawing:
            x1, y1 = self.old_coords
            self.canvas.create_line(x, y, x1, y1,width=self.lineWidth)
            self.drawOnPillow(event.x, event.y, x1, y1)
            
        self.old_coords = x, y
        
    def drawOnPillow(self, x, y, x1, y1):
        #print('x y x1 y1', x, y, x1, y1)
        self.draw.line([x, y, x1, y1], fill=self.pencil, width=self.lineWidth)
        
    def savePillow(self, name='pillow.png'):
        self.img.save(name)
        
    def onKeyDown(self, event):
        if event.char == 's':
            self.savePillow()
        elif event.char == 'q':
            print('quit')
            self.root.destroy()
        
    def __init__(self, root, width, height, lineWidth=5, bg=(255,255,255), pencil=(0,0,0)):
        self.trace = True
        self.width = width
        self.height = height
        self.bg = bg
        self.pencil = pencil
        self.img = None
        self.draw = None
        self.root = root
        self.lineWidth=lineWidth

        
root = tk.Tk()
draw = DrawableArea(root, 200, 200, bg=(0,0,0), pencil=(255,255,255))
draw.start()
root.mainloop()