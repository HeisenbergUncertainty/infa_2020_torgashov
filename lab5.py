# coding: utf8
from random import randrange as rnd, choice
import tkinter as tk
import math
import time
 
 
 
root = tk.Tk()
fr = tk.Frame(root)
root.geometry('1200x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
g = 3 #îòâå÷àåò çà ãðàâèòàöèþ
kv = 0.7 #êîýôôèöèåíò íà÷àëüíîé ñêîðîñòè øàðà, èçìåíÿåòñÿ äëÿ "ïîäêðó÷èâàíèÿ" áàëëèñòèêè
start_r = 45 #start_r è sub_r ñëóæàò äëÿ èçìåíåíèÿ ïàðàìåòðîâ öåëè ñî âðåìåíåì. Èçìåíÿþòñÿ â target.hit
sub_r = 0
colors = ['blue', 'green', 'red', 'yellow']
points = 0
 
 
class ball():
    def __init__(self, x=40, y=450):
        """ Êîíñòðóêòîð êëàññà ball
 
        Args:
        x - íà÷àëüíîå ïîëîæåíèå ìÿ÷à ïî ãîðèçîíòàëè
        y - íà÷àëüíîå ïîëîæåíèå ìÿ÷à ïî âåðòèêàëè
        r - ðàäèóñ ìÿ÷à
        vx - íà÷àëüíàÿ ñêîðîñòü ìÿ÷à ïî ãîðèçîíòàëè
        vy - íà÷àëüíàÿ ñêîðîñòü ìÿ÷à ïî âåòðèêàëè
        live - âðåìÿ æèçíè
        color - öâåò øàðà
        id - ñîîòâåòñâóþùàÿ ôèãóðà èç canv
        global colors - ñïèñîê öâåòîâ
        """
        global colors
        self.x = x
        self.y = y
        self.r = 5
        self.vx = 0
        self.vy = 0
        self.color = choice(colors)
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 50
 
    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )
 
    def move(self):
        global g
        """Ïåðåìåñòèòü ìÿ÷ ïî ïðîøåñòâèè åäèíèöû âðåìåíè.
 
        Îáíîâëåíèå êîîðäèíàòû ñî âðåìåíåì, îáíîâëåíèå ñêîðîñòè ìÿ÷à è óäàëåíèå ìÿ÷à,
        åñëè òîò âûëåòàåò çà íèæíþþ èëè ïðàâóþ ãðàíèöó ïîëÿ. Òàêæå óäàëåíèå øàðà ïî âðåìåíè
        îò ïàðàìåòðà live, èëè åãî óìåíüøåíèå
        """
        self.x += self.vx
        self.y -= self.vy
        self.vy -= g
        self.set_coords()
        if self.x > 1200 or self.y > 600:
            canv.delete(self.id)
        if self.live < 0:
            balls.pop(balls.index(self))
            canv.delete(self.id)
        else:
            self.live -= 1
 
    def hittest(self, obj):
        """Ôóíêöèÿ ïðîâåðÿåò ñòàëêèâàëêèâàåòñÿ ëè äàííûé îáüåêò ñ öåëüþ, îïèñûâàåìîé â îáüåêòå obj.
 
        Args:
            obj: Îáüåêò, ñ êîòîðûì ïðîâåðÿåòñÿ ñòîëêíîâåíèå.
        Returns:
            Âîçâðàùàåò True â ñëó÷àå ñòîëêíîâåíèÿ ìÿ÷à è öåëè. Â ïðîòèâíîì ñëó÷àå âîçâðàùàåò False.
 
        ðåàëèçîâàíà ñ ïîìîùüþ òðåóãîëüíèêà ñ êîîðäèíàòàìè
        (self.x, self.y)
        (self.x - self.vx, self.y - self.vy)
        (obj.x, obj.y)
 
        a,b,c - ñòîðîíû òðåóãîëüíèêà
        p - ïîëóïåðèìåòð
        s - ïëîùàäü
        h - âûñîòà èç âåðøèíû ñ öåëüþ(ïðîòèâ ñòîðîíû a)
        r - ïðèöåëüíûé ïàðàìåòð (ñóììà ðàäèóñîâ)
        cosb - êîñèíóñ ïðîòèâ ñòîðîíû b, óìíîæåííûé íà a*c
        cosc - êîñèíóñ ïðîòèâ ñòîðîíû c, óìíîæåííûé íà a*b
        """

        a = ((self.vx) ** 2 + (self.vy) ** 2) ** 0.5
        c = ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5
        b = ((self.x - self.vx - obj.x) ** 2 + 
                (self.y - self.vy - obj.y) ** 2) ** 0.5
        p = (a + b + c)/2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        h = 2 * s / a
        r = self.r + obj.r
        cosb = (self.x - obj.x) * (self.vx) + (+self.y - obj.y) * (self.vy)
        cosc = (self.x - self.vx - obj.x) * (-self.vx) + \
                (self.y - self.vy - obj.y)*(-self.vy)
        return ((h < r) and (cosb >= 0) and (cosc >= 0)) \
                or (b < r) \
                or (c < r)
 
 
class gun():
    def __init__(self):
        """
        Èíèöèàëèçàöèÿ ðóæüÿ
        """
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420,
                width=5, arrow=tk.LAST) 
 
    def fire2_start(self, event):
        self.f2_on = 1
 
    def fire2_end(self, event):
        """Âûñòðåë ìÿ÷îì.
 
        Ïðîèñõîäèò ïðè îòïóñêàíèè êíîïêè ìûøè.
        Íà÷àëüíûå çíà÷åíèÿ êîìïîíåíò ñêîðîñòè ìÿ÷à vx è vy çàâèñÿò îò ïîëîæåíèÿ ìûøè.
        balls - ñïèñîê âñåõ ìÿ÷åé
        bullet_1 - ñ÷åò ìÿ÷åé íà ïåðâóþ öåëü(îáíóëÿåòñÿ ïîñëå ïîïàäàíèÿ)
        bullet_2 - ñ÷åò ìÿ÷åé íà âòîðóþ öåëü(îáíóëÿåòñÿ ïîñëå ïîïàäàíèÿ)
        kv - êîýôôèöèåíò íà÷àëüíîé ñêîðîñòè øàðà, èçìåíÿåòñÿ äëÿ "ïîäêðó÷èâàíèÿ" áàëëèñòèêè
        """
        global balls, bullet_1, bullet_2, kv
        bullet_1 += 1
        bullet_2 += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an) * kv
        new_ball.vy = - self.f2_power * math.sin(self.an) * kv
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10
 
    def targetting(self, event=0):
        """Ïðèöåëèâàíèå. Çàâèñèò îò ïîëîæåíèÿ ìûøè."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )
 
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
 
 
canv_points = canv.create_text(50, 50,
                text = points, font=("impact", 44))
 
 
class target():
    def __init__(self, input_color):
        """
        Èíèöèàëèçàöèÿ öåëè-1
        points - áàëëîâ ïîëó÷åíî çà ýòó öåëü
        vx - íà÷àëüíàÿ ñêîðîñòü ìÿ÷à ïî ãîðèçîíòàëè
        time - ïàðàìåòð äëÿ êîëåáàíèé öåëè
        is_hitted - ïðîâåðêà, ïîïàëè â öåëü èëè íåò(íóæíà äëÿ îñòàíîâêè target.self_coords())
        """
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.vy = rnd(-5, 5)
        self.color = input_color
        self.new_target()
        self.time = 0
        self.is_hitted = False
 
 
    def new_target(self):
        """ Èíèöèàëèçàöèÿ íîâîé öåëè. 
        x - êîîðäèíàòà ïî ãîðèçîíòàëè. Ñëó÷àéíàÿ.
        y - êîîðäèíàòà ïî âåðòèêàëè. Ñëó÷àéíàÿ.
        r - ðàäèóñ. Ñëó÷àéíûé, íî çàâèñèò îò ãëîáàëüíûõ start_r, sub_r
        Îáíîâëåíèå vy, ïðîâåðêà, ÷òî îíà íåíóëåâàÿ
        """
        global start_r, sub_r
        x = self.x = rnd(600, 1080)
        y = self.y = rnd(200, 500)
        r = self.r = rnd(start_r, 50 - sub_r)
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=self.color)
        while self.vy == 0:
            self.vy = rnd(-5, 5)
        self.is_hitted = False
 
    def hit(self, pointss=1):
        """Ïîïàäàíèå øàðèêà â öåëü.
        Ôëàæîê is_hitted â True
        Èçìåíåíèå ãëáàëüíûõ start_r, sub_r
        Îáíîâëåíèå î÷êîâ çà ýòó öåëü
        """
        global start_r, sub_r, points, canv_points
        self.is_hitted = True
        canv.coords(self.id, -10, -10, -10, -10)
        points += pointss
        canv.itemconfig(canv_points, text = points)
        start_r -= 5
        if start_r <= 0:
            start_r = 5
        sub_r += 4
        if sub_r >= 44:
            sub_r = 44
      
    def set_coords(self):
        if not self.is_hitted:
            canv.coords(
                    self.id,
                    self.x - self.r,
                    self.y - self.r,
                    self.x + self.r,
                    self.y + self.r
            )
 
    def move(self):
        if self.time == 30:
            self.time = 0
            self.vy = -self.vy
        self.y += self.vy
        self.time += 1
        self.set_coords()
 
 
t1 = target('red')
t2 = target('blue')
screen1 = canv.create_text(600, 30, text='', font=("impact", 20))
screen2 = canv.create_text(600, 60, text='', font=("impact", 20))
g1 = gun()
bullet_1 = 0
bullet_2 = 0
balls = []
 
 
def new_game(event=''):
    global gun, t1, t2, screen1, screen2, balls, bullet_1, bullet_2
    t1.new_target()
    t2.new_target()
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
 
    z = 0.03
    t1.live = 1
    t2.live = 1
    while t1.live or balls or t2.live:
        t1.move()
        t2.move()
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                if (bullet_1 == 0):
                    canv.itemconfig(screen1, text='Öåëü-1 ïîãèáëà ñðàçó!')
                else:
                    canv.itemconfig(screen1, text='Âû óíè÷òîæèëè öåëü-1 çà ' \
                        + str(bullet_1) + ' âûñòðåë(à)(îâ)')
                canv.update()
                bullet_1 = 0
                
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
                if (bullet_2 == 0):
                    canv.itemconfig(screen2, text='Öåëü-2 ïîãèáëà ñðàçó.')
                else:
                    canv.itemconfig(screen2, text='Âû óíè÷òîæèëè öåëü-2 çà ' \
                        + str(bullet_2) + ' âûñòðåë(à)(îâ)')
                canv.update()
                bullet_2 = 0
                
        if (t1.live == 0):
            t1.new_target()
            t1.live = 1
        if (t2.live == 0):
            t2.new_target()
            t2.live = 1
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
 
    canv.itemconfig(screen1, text='')
    canv.itemconfig(screen2, text='')
    canv.delete(gun)
    if (t1.live == 0) and (t2.live == 0):
        root.after(100, new_game())
 
new_game()
 
mainloop()
