#基类必须继承于object,否则在派生类中将无法使用super()函数
class Person(object):
      def __init__(self,name='',age=20,sex='man'):
            self.setName(name)
            self.setAge(age)
            self.setSex(sex)

      def setName(self,name):
            if not isinstance(name,str):
                  print('name must be string.')
                  self.__name = ''
                  return
            self.__name = name

      def setAge(self,age):
            if type(age) != int:
                  print('age must be integer.')
                  self.__age = 20
                  return
            self.__age = age

      def setSex(self,sex):
            if sex not in('man','woman'):
                  print('sex must be "man" or "woman"')
                  self.__sex = 'man'
                  return
            self.__sex = sex

      def show(self):
            print(self.__name, self.__age, self.__sex, sep = '\n')


#派生类
class Teacher(Person):
      def __init__(self, name='',age = 30, sex = 'man',department = 'Computer'):
            #调用基类构造方法初始化基类的私有数据成员
            super(Teacher,self).__init__(name,age,sex)
            #也可以这样初始化基类的私有数据成员
            #Person.__init__(self,name,age,sex)
            #初始化派生类的数据成员
            self.setDepartment(department)

      def setDepartment(self, department):
            if type(department)!= str:
                  print('department must be a string.')
                  self.__department = 'Computer'
                  return
            self.__department = department

      def show(self):
            super(Teacher,self).show()
            print(self.__department)

if __name__ == '__main__':
      #创建基类对象
      zhangsan = Person('zhang San', 19, 'man')
      zhangsan.show()
      print('='*30)

      #创建派生类对象
      lisi = Teacher('Li Si',32,'man','Math')
      lisi.show()

      #调用继承的方法修改年龄
      lisi.setAge(40)
      lisi.show()
