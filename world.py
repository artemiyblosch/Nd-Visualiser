import tkinter as tk
from time import sleep
from PIL import Image,ImageDraw,ImageTk

class World:
    def __init__(self, projections : list[tuple[float, float]], size : tuple[int,int], bg : str, domain : tuple[tuple[int],tuple[int]]):
        self.projections = projections
        self.size = size
        self.bg = bg
        self.domain = domain

        self.root = tk.Tk()
        self.root.geometry(f"{self.size[0]}x{self.size[1]}")
        self.canvas = tk.Canvas(width=self.size[0],height=self.size[1], bg=self.bg)
        self.canvas.place(x=0,y=0)

        self.image = Image.new('RGBA',self.size,(0,0,0,0))
        self.draw = ImageDraw.Draw(self.image)
    
    def project_point(self, point : list[float]):
        for p in self.projections[::-1]:
            point = p(point)
        return point
    
    def flush(self):
        #image = ImageTk.PhotoImage(image=self.image,size=self.size)
        #self.canvas.create_image(0, 0, image=image, anchor="nw")
        #self.image.save("image.png")
        self.image.save("image.png")
        img = ImageTk.PhotoImage(Image.open("image.png"))
        self.canvas.create_image(10,10,anchor=tk.NW,image=img)
        self.image = Image.new('RGB',self.size,(255,255,255))
        self.draw = ImageDraw.Draw(self.image, "RGBA")
    
    def convert_point(self,point : tuple[float, float]):
        p_x = (point[0]-self.domain[0][0])\
               /(self.domain[0][1]-self.domain[0][0])\
               *(self.size[0])
        p_y = (point[1]-self.domain[1][0])\
               /(self.domain[1][1]-self.domain[1][0])\
               *(self.size[1])
        return (p_x,p_y)

    def draw_face(self, points : list[list[float]], color : tuple[int,int,int]):
        points = [self.convert_point(self.project_point(i)) for i in points]
        self.draw.polygon(xy = points,\
                          fill=((*color,50) if color[0] != -1 else (0,0,0,0)),\
                          outline=((*color,254) if color[0] != -1 else (0,0,0,254)))
        #self.canvas.create_polygon(*points, outline='#%02x%02x%02x' % color, fill="")
    
    def clear(self): 
        self.canvas.delete("all")
    
    def mainloop(self,frame_f = None, f_del : float = 0):
        if frame_f == None:
            self.flush()
            self.root.mainloop()
            return
        
        while 1:
            sleep(f_del)
            self.flush()
            self.root.update()
            frame_f()