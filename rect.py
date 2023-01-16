
from pygame import*
import random
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self,x,y,w,h):
        sprite.Sprite.__init__(self)
        self.rect=Rect(x,y,w,h)
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        draw.rect(window,self.color,self.rect)
class Object(sprite.Sprite):
    def __init__(self,color,x,y,w,h):
        super().__init__()
        self.color=color
        self.width=w
        self.height=h
        self.image=Surface((self.width,self.height))
        self.image.fill((self.color))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
Red=(255,0,0)
Green=(0,255,0)
Blue=(0,0,255)
Yellow=(255,255,0)
bg= (25,55,88)
window=display.set_mode((700,500))
window.fill(bg)
FPS=60
clock=time.Clock()
rect1=Object(Red,200,120,150,150)
rect2=Object(Green,370,120,150,150)
rect3=Object(Blue,200,290,150,150)
rect4=Object(Yellow,370,290,150,150)
rects=[rect1,rect2,rect3,rect4]
point=0
words=['красный','зелёный','синий','жёлтый']
colors=[Red,Green,Blue,Yellow]
random_color=random.choice(colors)
random_word=random.choice(words)
font.init()
font=font.SysFont('Arial',60)
end=font.render('Время вышло!',True,(0,0,0))
score_in_end=font.render('Ваш счёт:'+str(point),True,(0,0,0))
text=font.render(random_word,True,random_color)
counter = 30
text_time = font.render(str(counter), True, (0, 128, 0))
timer_event = USEREVENT+1
time.set_timer(timer_event, 1000)
final=False
finish=False
run=True
while run:
    for e in event.get():
        if e.type==QUIT:
            run=False
        if e.type==MOUSEBUTTONDOWN and e.button==1:
            x,y=e.pos
            for i in range(4):
                if rects[i].collidepoint(x,y):
                    if rects[i].color==random_color:
                        if final==False:
                            point+=1
                            random_color=random.choice(colors)
                            random_word=random.choice(words)
                            text=font.render(random_word,True,random_color)
                    else:
                        if point>=1:
                            if final==False:
                                point-=1                        
        elif e.type == timer_event:
            counter -= 1
            text_time = font.render(str(counter), True, (0, 128, 0))
    score=font.render('счёт:'+str(point),True,(255,0,255))
    if counter<0:
        score_in_end=font.render('Ваш счёт:'+str(point),True,(0,0,0))
        final=True
        finish=True
        window.fill(bg)
        window.blit(end,(170,100))
        window.blit(score_in_end,(200,250))
    if finish!= True:
        window.fill(bg)
        rect1.draw()
        rect2.draw()
        rect3.draw()
        rect4.draw()
        window.blit(text,(0,0))
        window.blit(text_time,(340,0))
        window.blit(score,(525,0))
    display.update()
    clock.tick(FPS)