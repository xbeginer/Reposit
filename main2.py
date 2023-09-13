import random
from tkinter import *
window = Tk()
w = 610
h = 610
window.geometry(f"{w}x{h}")
canvas = Canvas(window, width=w, height=h, border=True, bg="red")
canvas.place(x=0, y=0)
bg_photo = PhotoImage(file="замок.png")
class Knight():
    def __init__(self):
        self.x = 70
        self.y = h // 2
        self.v = 0
        self.v_x = 0
        self.photo = PhotoImage(file="рыцарь.png")
    def up(self, event):
        self.v = -3
    def down(self, event):
        self.v = 3
    def left(self, event):
        self.v_x = -3
    def right(self, event):
        self.v_x = 3
    def stop(self, event):
        self.v = 0
        self.v_x = 0

class Dragon:
    def __init__(self):
        self.x = 750
        self.y = random.randint(100, 500)
        self.v = random.randint(1, 3)
        self.photo = PhotoImage(file="дракон.png")

knight = Knight()
dragons = [Dragon() for i in range(1)]

def game():
    canvas.delete('all')
    canvas.create_image(300, 300, image=bg_photo)
    canvas.create_image(knight.x, knight.y, image=knight.photo)
    knight.y += knight.v
    knight.x += knight.v_x
    current = 0
    dragon_to_kill = -1
    for d in dragons:
        d.x -= d.v
        canvas.create_image(d.x, d.y, image=d.photo)
        if ((d.x - knight.x) ** 2) + ((d.y - knight.y) ** 2) <= (96) ** 2:
            dragon_to_kill = current
        current += 1
        if d.x <= 0:
            canvas.delete('all')
            canvas.create_text(w // 2, h // 2, text="You lose!", font="Verdana 42", fill='white')
            break

    if dragon_to_kill >= 0:
        del dragons[dragon_to_kill]
    if len(dragons) == 0:
        canvas.delete('all')
        canvas.create_text(w // 2, h // 2, text="You Win!", font="Verdana 42", fill='white')
    else:
        window.after(5, game)

    if knight.y <= 52:
        knight.y = 53
    if knight.y >= 41:
        knight.y = 40
    if knight.x <= 10:
        knight.x = 10
    if knight.x >= 100:
        knight.x = 100
    window.after(5, game)

game()
window.bind("<Key-Up>", knight.up)
window.bind("<Key-Down>", knight.down)
window.bind("<Key-Right>", knight.right)
window.bind("<Key-Left>", knight.left)
window.bind("<KeyRelease>", knight.stop)
window.mainloop()