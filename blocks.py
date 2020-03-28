
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
re = 'n'
while 1:
    move_Speed+=0.01
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
             pygame.quit()
             print("Your score=%d"%(int(cur_time-init_time)))
             print("Do you want to restart?[y/n]")
             judge = False
             re = input()
             break;
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
        pygame.display.update()
        time.sleep(0.03)
        cur_time=time.time()

    if (re=='y' or re == 'Y'):
        print("1")
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
        continue
    if judge == False:
        break
        sys.exit()
        



