__metaclass__ = type

class Bird:
      def __init__(self):
            self.hungry = True
      def eat(self):
            if self.hungry:
                  print('Aaaaaah....')
                  self.hungry = False
            else:
                  print('NO,thanks!')
class SongBird(Bird):
      def __init__(self):
           # Bird.__init__(self)#调用未绑定的超类构造方法
           super(SongBrid,self).__init__()#新式类的调用父类的构造方法
            self.sound = 'Squawk!'
      def sing(self):
            print (self.sound)
            
