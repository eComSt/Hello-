from tkinter import *
from random import randint

window = Tk()
window.geometry("600x600")

class nuck:
    image = PhotoImage(file = r"elements/neg.jpg").subsample(4,4)

class fig:
    image = PhotoImage(file = r"elements/nuck.jpg").subsample(4,4)
    def add(self,other):
        if isinstance(other,nuck):
            return nill

class nill:
    image = PhotoImage(file = r"elements/nillnicknate.jpg").subsample(4,4)
    def add(self,other):
        if isinstance(other,nuck):
            return nill
canvas = Canvas(window, width = 600, height = 600)
canvas.pack()

elements = [nuck(), fig(), nill()]
for elem in elements:
    canvas.create_image(randint(50,550),randint(50,550),image = elem.image)

def move(event):
    images_id = canvas.find_overlapping(event.x,event.y,event.x+10,event.y+10)
    if len(images_id)>1:
        el_1 = images_id[0]
        el_2 = images_id[1]
        element1 = elements[el_1-1]
        element2 = elements[el_2-1]
    new_elem = element1 + element2
    if new_elem not in elements:
        canvas.create_image(randint(50,550),randint(50,550),image = new_elem.image)
        elements.append(new_elem)
    canvas.coords(images_id,event.x,event.y)

window.bind("",move)
window.mainloop()
