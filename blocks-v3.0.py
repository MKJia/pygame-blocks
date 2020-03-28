
import pygame, sys, time
import random
from pygame.locals import *

#判断碰撞
def do_Rects_Overlap(rect1,rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        if((is_Point_Inside_Rect(a.left, a.top, b))or
            (is_Point_Inside_Rect(a.left, a.bottom, b)) or
            (is_Point_Inside_Rect(a.right, a.top, b)) or
            (is_Point_Inside_Rect(a.right, a.bottom, b))):
            return True
    return False

def is_Point_Inside_Rect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top ) and (y < rect .bottom):
        return True
    else:
        return False

def button (msg, x, y, w, h, ic, ac):
    mouse =pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(window_Surface, ac, (x,y,w,h))
    else:
        pygame.draw.rect(window_Surface, ic, (x,y,w,h))
    smallText = pygame.font.SysFont("arial", 23)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)))
    window_Surface.blit(textSurf, textRect)


def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def loadtext(score,high,xloc,yloc,fontsize):          
    my_font=pygame.font.SysFont('arial',fontsize)
    textstr='score:'+str(score)+'    '+'highest score:'+str(high)
    text_screen=my_font.render(textstr, True, WHITE)
    window_Surface.blit(text_screen, (xloc,yloc))

def loadinittext():          
    my_font=pygame.font.SysFont('arial',30)
    textstr='Insist over 30s for only GENIUS!!!'
    text_screen=my_font.render(textstr, True, WHITE)
    window_Surface.blit(text_screen, (15,100))

def loadhelptext():          
    my_font=pygame.font.SysFont('arial',20)
    textstr='GENIUS NEEDS NO HELP!!!'
    text_screen=my_font.render(textstr, True, WHITE)
    window_Surface.blit(text_screen, (25,200))
    
pygame.init()


window_Width = 400
window_Height = 400




window_Surface = pygame.display.set_mode((window_Width, window_Height), 0, 32)

pygame.display.set_caption("Caiji J's game")

down_Left = 1
down_Right = 3
up_Left = 7
up_Right = 9


move_Speed = 2
Black = (0, 0, 0)
RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (217,182,18)
WHITE = (255,255,255)
bright_green = (0,200,0)

b1 = {'rect':pygame.Rect(300, 80, 50, 100),'color':RED, 'dir':up_Right} #红长方形
b2 = {'rect':pygame.Rect(120, 200, 20, 20),'color':GREEN, 'dir':up_Left}#绿
b3 = {'rect':pygame.Rect(100, 150, 60, 60),'color':BLUE, 'dir':down_Left}#蓝
b4 = {'rect':pygame.Rect(350, 350, 40, 40),'color':YELLOW, 'dir':down_Left}#黄
blocks = [b1, b2, b3]
move_block =[b4]
judge = True
re = 'n'
i=1
high = 0

while judge:
    while True:
        x, y = pygame.mouse.get_pos()
        # print(x)
        judge = False
        loadinittext()
        
        button("Help", 50,250,100,50, GREEN, bright_green)
        button("Start Game", 250,250,100,50, GREEN, bright_green)
        pygame.display.update()
        for event in pygame.event.get():#获得事件
            if event.type==pygame.MOUSEBUTTONDOWN and 50<=x<=150 and 250<=y<=300:
                loadhelptext()
                pygame.display.update()
                break
            if event.type==pygame.MOUSEBUTTONDOWN and 250<=x<=350 and 250<=y<=300:
                judge = True
                pygame.mouse.set_visible(False)
                break
        if judge:
            init_time=time.time()
            cur_time=init_time
            break
            
            
    while judge:
        if move_Speed <14:
            move_Speed+=0.015
            print(move_Speed)
        center=(100,100)
        move_Speed = move_Speed+0.0001 
        window_Surface.fill(Black)
        x, y = pygame.mouse.get_pos()
        b4 = {'rect':pygame.Rect(x-20,y-20, 40,40),'color':YELLOW, 'dir':down_Left}#黄
        pygame.draw.rect(window_Surface, b4['color'], b4['rect'])
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        for b in blocks:
            if do_Rects_Overlap(b4['rect'], b['rect']):
                score = int(cur_time-init_time)
                if high < score:
                    high = score
                while True:
                    x, y = pygame.mouse.get_pos()
                    # print(x)
                    judge = False
                    window_Surface.fill(Black)
                    loadinittext()
                    loadtext(score,high,70,150,30)
                    pygame.mouse.set_visible(True)
                    button("Try Again", 250,250,100,50, GREEN, bright_green)
                    button("Quit Game", 250,310,100,50,GREEN, bright_green)
                    pygame.display.update()
                    for event in pygame.event.get():#获得事件
                        if event.type==pygame.MOUSEBUTTONDOWN and 250<=x<=350 and 250<=y<=300:
                            judge = True
                            re='y'
                            break
                        if event.type==pygame.MOUSEBUTTONDOWN and 250<=x<=350 and 310<=y<=360:
                            pygame.quit()
                            break
                    if judge:
                        init_time=time.time()
                        cur_time=init_time
                        break
                
            #移动
            if b['dir'] == down_Left:
                b['rect'].left -= move_Speed
                b['rect'].top += move_Speed
            if b['dir'] == down_Right:
                b['rect'].left += move_Speed
                b['rect'].top += move_Speed
            if b['dir'] == up_Left:
                b['rect'].left -= move_Speed
                b['rect'].top -= move_Speed
            if b['dir'] == up_Right:
                b['rect'].left += move_Speed
                b['rect'].top -= move_Speed
    #反弹
            if b['rect'].top < 0:
                if b['dir'] == up_Left:
                    b['dir'] = down_Left
                if b['dir'] == up_Right:
                    b['dir'] = down_Right
            if b['rect'].bottom > window_Height:
                if b['dir'] == down_Left:
                    b['dir'] = up_Left
                if b['dir'] == down_Right:
                    b['dir'] = up_Right
            if b['rect'].left < 0:
                if b['dir'] == down_Left:
                    b['dir'] = down_Right
                if b['dir'] == up_Left:
                    b['dir'] = up_Right
            if b['rect'].right > window_Width:
                if b['dir'] == down_Right:
                    b['dir'] = down_Left
                if b['dir'] == up_Right:
                    b['dir'] = up_Left
            pygame.draw.rect(window_Surface, b['color'], b['rect'])

    #重置
        if judge:
            cur_time=time.time()
            loadtext(int(cur_time-init_time),high,120,0,22)
            pygame.display.update()
            time.sleep(0.03)
        if (re=='y' or re == 'Y'):
            pygame.init()

            init_time=time.time()
            cur_time=init_time
            window_Width = 400
            window_Height = 400



            window_Surface = pygame.display.set_mode((window_Width, window_Height), 0, 32)

            pygame.display.set_caption("Caiji J's game")

            down_Left = 1
            down_Right = 3
            up_Left = 7
            up_Right = 9


            move_Speed = 2
            Black = (0, 0, 0)
            RED = (255, 0, 0)
            GREEN =(0, 255, 0)
            BLUE = (0, 0, 255)
            YELLOW = (217,182,18)
            WHITE = (255,255,255)

            b1 = {'rect':pygame.Rect(300, 80, 50, 100),'color':RED, 'dir':up_Right} #红长方形
            b2 = {'rect':pygame.Rect(120, 200, 20, 20),'color':GREEN, 'dir':up_Left}#绿
            b3 = {'rect':pygame.Rect(100, 150, 60, 60),'color':BLUE, 'dir':down_Left}#蓝
            b4 = {'rect':pygame.Rect(350, 350, 40, 40),'color':YELLOW, 'dir':down_Left}#黄
            blocks = [b1, b2, b3]
            move_block =[b4]
            judge = True
            re ='n'
            break
        if judge == False:
            break
        



