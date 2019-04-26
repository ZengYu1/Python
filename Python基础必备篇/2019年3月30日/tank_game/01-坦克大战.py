# -*- coding: utf-8 -*-
# @Author: Zengyu
# @Date:   2019-03-30 23:31:12
# @Last Modified by:   Zengyu
# @Last Modified time: 2019-03-30 23:59:28
import pygame
import sys,time
from random import randint
from pygame.locals import *

"""坦克大战主窗口"""
class TankMain(object):
    width=500
    height=500
    my_tank_missile_list = []
    my_tank = None
    # enemy_list = []
    wall = None

    enemy_list=pygame.sprite.Group()#敌方坦克的族群
    explode_list=[]
    enemy_missile_list=pygame.sprite.Group()


	#开始游戏的方法
    def startGame(self):
        pygame.init()#pygame模块初始化，加载系统资源
        #创建一个屏幕，屏幕的大小（宽，高），窗口的特性(0,RESIZEBLE,FULLSCREEM)
        screem=pygame.display.set_mode((TankMain.width,TankMain.height),0,32)
        #给窗口设置一个标题
        pygame.display.set_caption("坦克大战")

        #创建一堵墙
        TankMain.wall=Wall(screem,65,160,30,120)

        TankMain.my_tank=My_Tank(screem)#创建一个我方坦克

        if len(TankMain.enemy_list) == 0:
            for i in range(1,6):
                TankMain.enemy_list.add(Enemy_Tank(screem))#把敌方坦克放到组里



        while True:
            if len(TankMain.enemy_list) < 5:
                TankMain.enemy_list.add(Enemy_Tank(screem))
            #设置屏幕的背景色为黑色
            screem.fill((0,0,0))
            #显示左上角的文字
            for i, text in enumerate(self.write_text(),1):
                screem.blit(text,(0,5+(15*i)))
            # 显示游戏中的墙并且对墙和其他对象进行碰撞检测
            TankMain.wall.display()
            TankMain.wall.hit_other()

            self.get_event(TankMain.my_tank,screem)#获取事件，根据获取的事情处理
            if TankMain.my_tank:
                TankMain.my_tank.hit_enemy_missile()#我方坦克和敌方的炮弹进行碰撞检测
            if TankMain.my_tank and TankMain.my_tank.live:
                #显示我方坦克
                TankMain.my_tank.display()#在屏幕上显示我方坦克
                TankMain.my_tank.move()
            else:
                TankMain.my_tank=None



            #显示和随机移动敌方坦克
            for enemy in TankMain.enemy_list:
                enemy.display()
                enemy.random_move()
                enemy.random_fire()

            #显示所有的我方炮弹
            for m in TankMain.my_tank_missile_list:
                if m.live:
                    m.display()
                    m.hit_tank()#炮弹打中敌方坦克
                    m.move()
                else:
                    TankMain.my_tank_missile_list.remove(m)

            # 显示所有的敌方炮弹
            for m in TankMain.enemy_missile_list:
                if m.live:
                    m.display()
                    # m.hit_tank()  # 炮弹打中敌方坦克
                    m.move()
                else:
                    TankMain.enemy_missile_list.remove(m)

            for explode in TankMain.explode_list:
                explode.display()

            #显示重置
            time.sleep(0.05)#每次休眠，跳到下一帧
            pygame.display.update()


    # 获取所有的事件
    def get_event(self,my_tank,screem):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.stopGame()
            if event.type == KEYDOWN and (not my_tank) and event.key ==K_n:
                TankMain.my_tank=My_Tank(screem)

            if event.type == KEYDOWN and my_tank:
                if event.key == K_LEFT or event.key == K_a:
                    my_tank.direction="L"
                    my_tank.stop=False
                    # my_tank.move()
                if event.key == K_RIGHT or event.key == K_d:
                    my_tank.direction="R"
                    my_tank.stop=False
                    # my_tank.move()
                if event.key == K_UP or event.key == K_w:
                    my_tank.direction = "U"
                    my_tank.stop=False
                    # my_tank.move()
                if event.key == K_DOWN or event.key == K_s:
                    my_tank.direction = "D"
                    my_tank.stop=False
                    # my_tank.move()
                if event.key == K_ESCAPE:
                    self.stopGame()
                if event.key == K_SPACE:
                    m = my_tank.fire()
                    m.good=True#我方坦克发射的炮弹
                    TankMain.my_tank_missile_list.append(m)
            if event.type == KEYUP and my_tank:
                if event.key==K_LEFT or event.key==K_RIGHT or event.key==K_UP or event.key==K_DOWN:
                    my_tank.stop=True
	#关闭游戏


    def stopGame(self):
        sys.exit()

    # 在屏幕的左上角显示文字内容
    def write_text(self):
        font = pygame.font.SysFont("simsunnsimsun",12)#定义一个字体
        text_sf1 = font.render("敌方坦克数量为:%d"%len(TankMain.enemy_list),True,(255,0,0))#根据字体创建一个文件的图像
        text_sf2 = font.render("我方坦克炮弹的数量:%d"%len(TankMain.my_tank_missile_list),True,(255,0,0))#根据字体创建一个文件的图像
        return text_sf1,text_sf2      #返回文字图像

#坦克大战游戏中所有对象的父类
class BaseItem(pygame.sprite.Sprite):

    def __init__(self,screem):
        pygame.sprite.Sprite.__init__(self)
        #所有对象共享的属性
        self.screem=screem #坦克在移动或者显示过程中需要用到当前游戏的屏幕

    #在游戏屏幕中显示当前游戏对象
    def display(self):
        if self.live:
            self.image=self.images[self.direction]
            self.screem.blit(self.image,self.rect)

class Tank(BaseItem):
    #定义类属性，所有坦克对象高和宽都是一样的
    width=50
    height=50
    rect=None
    def __init__(self,screem,left,top):
        super().__init__(screem)
        self.direction='D'  #坦克的方向默认向下（上下左右）
        self.speed=5#坦克移动的速度
        self.stop=False
        self.images={}
        self.images["L"]=pygame.image.load("images/tankL.gif")
        self.images["R"]=pygame.image.load("images/tankR.gif")
        self.images["U"]=pygame.image.load("images/tankU.gif")
        self.images["D"]=pygame.image.load("images/tankD.gif")
        self.image=self.images[self.direction]#坦克的图片由方向决定
        self.rect=self.image.get_rect()
        self.rect.left=left
        self.rect.top=top
        self.live =True#绝对坦克是否消灭了
        self.oldtop=self.rect.top
        self.oldleft=self.rect.left

    def stay(self):
        self.rect.top=self.oldtop
        self.rect.left=self.oldleft

    def move(self):
        if not self.stop:#如果坦克不是停止状态
            self.oldleft=self.rect.left
            self.oldtop=self.rect.top
            if self.direction=="L":
                if self.rect.left > 0: #判断坦克是否在在屏幕最左边的位置
                    self.rect.left-=self.speed
                else:
                    self.rect.left=0
            elif self.direction=="R":#如果坦克方向向右，坦克的right增加就ok了
                if self.rect.right < TankMain.width:#坦克已经在屏幕的最右边的话就不能往右移动了
                    self.rect.right+=self.speed
                else:
                    self.rect.right=TankMain.width
            elif self.direction=="D":#坦克方向向下，坦克的bottom增加
                if self.rect.bottom < TankMain.height:
                    self.rect.top+=self.speed
                else:
                    self.rect.bottom=TankMain.height
            elif self.direction=="U":#坦克方向向上，top减小
                if self.rect.top > 0:
                    self.rect.top-=self.speed
                else:
                    self.rect.top=0

    def fire(self):
        m = Missile(self.screem,self)
        return m


class My_Tank(Tank):
    def __init__(self,screem):
        super().__init__(screem,275,400)#创建一个我方坦克，坦克显示在屏幕的中下部位置
        self.stop=True
        self.live=True

    def hit_enemy_missile(self):
        hit_list=pygame.sprite.spritecollide(self,TankMain.enemy_missile_list,False)
        for m in hit_list:#我方坦克中弹
            m.live=False
            TankMain.enemy_missile_list.remove(m)
            self.live=False
            explode=Explode(self.screem,self.rect)
            TankMain.explode_list.append(explode)

class Enemy_Tank(Tank):

    def __init__(self,screem):
        super().__init__(screem,randint(1,5)*100,200)
        self.step=8 #坦克按照某个方向连续移动的步数
        self.get_random_direction()
        self.speed=3




    def get_random_direction(self):
        r=randint(0,4)  # 得到一个坦克移动方向和停止的随机数
        if r == 4:
            self.stop = True
        elif r == 1:
            self.direction="L"
            self.stop = False
        elif r == 2:
            self.direction="R"
            self.stop = False
        elif r == 0:
            self.direction="D"
            self.stop = False
        elif r == 3:
            self.direction="U"
            self.stop = False

    #敌方坦克，按照一个确定随机方向，连续移动6步，然后才能再次改变方向
    def random_move(self):
        if self.live:
            if self.step==0:
                self.get_random_direction()
                self.step=6
            else:
                self.move()
                self.step-=1

    def random_fire(self):
        r = randint(0,50)
        if r == 45:
            m = self.fire()
            TankMain.enemy_missile_list.add(m)
        else:
            return


class Missile(BaseItem):
    width=12
    height=12
    def __init__(self,screem,tank):
        super().__init__(screem)
        self.tank=tank
        self.direction = tank.direction  #炮弹的方向由所发射的坦克方向决定
        self.speed = 12  # 炮弹移动的速度
        self.images = {} #炮弹所有的图片
        self.images["L"] = pygame.image.load("images/missileL.gif")
        self.images["R"] = pygame.image.load("images/missileR.gif")
        self.images["U"] = pygame.image.load("images/missileU.gif")
        self.images["D"] = pygame.image.load("images/missileD.gif")
        self.image = self.images[self.direction]  # 坦克的图片由方向决定
        self.rect = self.image.get_rect()
        self.rect.left = tank.rect.left + (tank.width-self.width)/2
        self.rect.top = tank.rect.top + (tank.height - self.height) / 2
        self.live = True  #炮弹是否消灭了
        self.good=False

    def move(self):
        if self.live:#如果炮弹还存在
            if self.direction=="L":
                if self.rect.left > 0: #判断坦克是否在在屏幕最左边的位置
                    self.rect.left-=self.speed
                else:
                    self.live=False
            elif self.direction=="R":#如果坦克方向向右，坦克的right增加就ok了
                if self.rect.right < TankMain.width:#坦克已经在屏幕的最右边的话就不能往右移动了
                    self.rect.right+=self.speed
                else:
                    self.live = False
            elif self.direction=="D":#坦克方向向下，坦克的bottom增加
                if self.rect.bottom < TankMain.height:
                    self.rect.top+=self.speed
                else:
                    self.live = False
            elif self.direction=="U":#坦克方向向上，top减小
                if self.rect.top > 0:
                    self.rect.top-=self.speed
                else:
                    self.live = False

    #炮弹击中坦克，第一中我方击中敌方坦克，敌方击中我方
    def hit_tank(self):
        if self.good:#如果炮弹是我方的
            hit_list = pygame.sprite.spritecollide(self, TankMain.enemy_list,False)
            for e in hit_list:
                e.live=False
                TankMain.enemy_list.remove(e)#如果敌方坦克被击中，则从列表中删除敌方坦克
                self.live=False
                explode=Explode(self.screem,e.ract)#产生一个爆照对象
                TankMain.explode_list.append(explode)


#爆照类
class Explode(BaseItem):

    def __init__(self,screem,rect):
        super().__init__(screem)
        self.live=True
        self.images= {pygame.image.load("images/0.png"),
                      pygame.image.load("images/1.png"),
                      pygame.image.load("images/2.png"),
                      pygame.image.load("images/3.png"),
                      pygame.image.load("images/4.png"),
                      pygame.image.load("images/5.png"),
                      pygame.image.load("images/6.png"),
                      pygame.image.load("images/7.png"),
                      pygame.image.load("images/8.png"),
                      pygame.image.load("images/9.png"),
                      pygame.image.load("images/10.png")}
        self.step=0
        self.rect=rect#爆照的位置和发生爆照前爆照碰到的坦克位置一样，在构造爆照的时候把坦克的rect传递进来

    #display方法在整个游戏运行过程中，循环调用，每隔0.05秒休眠一次
    def display(self):#在这里不用循环
        if self.live:
            if self.step == len(self.images):#意味着最后一张爆照图片已经显示了
                self.live=False
            else:
                self.image=self.images[self.step]
                self.screem.blit(self.image,self.rect)
                self.step+=1
        else:
            pass #删除该对象
#游戏中的墙
class Wall(BaseItem):
    def __init__(self,screem,left,top,width,height):
        super().__init__(screem)
        self.rect=Rect(left,top,width,height)
        self.color=(255,0,0)

    def display(self):
        self.screem.fill(self.color,self.rect)

    #针对墙和其他坦克或者炮弹的碰撞检测
    def hit_other(self):
        if TankMain.my_tank:
            is_hit=pygame.sprite.collide_rect(self,TankMain.my_tank)
            if is_hit:
                TankMain.my_tank.stop=True
                TankMain.my_tank.stay()
        if TankMain.enemy_list:
            hit_list=pygame.sprite.spritecollide(self,TankMain.enemy_list,False)
            for e in hit_list:
                e.stop=True
                e.stay()

game=TankMain()
game.startGame()








