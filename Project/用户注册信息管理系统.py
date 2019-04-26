#coding:gb2312
'''
用户注册信息管理系统
功能包括：
      1.查看全部已注册的用户信息
      2.查找用户信息
      3.修改用户信息
      4.删除用户信息
      5.添加新用户
      6.将用户信息存入文件
每个注册用户的信息用对象表示。程序启动时，自动载入文件中保存的用户信息
程序启动后。显示操作菜单，并根据选择执行不同的操作
各种菜单操作定义为函数，调用函数完成对于操作
'''
'''
导入pickle模块中的dump、load方法
dump方法将对象写入文件，load方法从文件载入对象
'''

from pickle import dump,load

## 定义user 类，实例对象的uname属性存储用户名，pwd属性存储登陆密码#######################
class user:
    #构造函数__init__()创建实例对象时初始化用户名和登陆密码，默认值为None
    def __init__(self,uname = None,pwd=None):
        self.uname = uname
        self.pwd = pwd

    #update()方法修改用户名和登陆密码
    def update(self,uname,pwd):
        self.uname = uname
        self.pwd = pwd

    #__repr()方法定义对象打印格式
    def __repr__(self):
        return 'username = %s \tpassword = %s' % (self.uname,self.pwd)
    ## user类代码结束

##函数showall()显示当前已经注册的用户信息################################
def showall():
    global userlist
    if len(userlist)==0:
        print('\t当前无注册用户')
    else:
        print('\t当前已注册用户信息如下：')
        n = 0
        for x in userlist:
            n += 1
            print('\t%s. '%n,x)
        input('\n\t按Enter键继续……\n')
        ##函数showall()代码结束

##函数check_update()执行查找、修改或删除操作##############################
def check_update():
    global userlist
    uname = input('\t请输入要查找的用户名:')
    index = find(uname)
    if index == -1:
        print('\t%s 不存在 ！'%uname)
    else:
        #用户名已注册，执行修改或删除操作
        print('\t%s 已经注册！'%uname)
        print('\t请选择操作：')
        print('\t 1.修改用户')
        print('\t 2.删除用户')
        op = input('\t请输入序号选择对应操作：')
        if op == '2':
            #删除用户
            del userlist[index]
            print('\n\t 已成功删除用户！')
        else:
            #修改用户信息
            uname = input('\t请输入新的用户名：')
            if uname == '':
                print('\t用户名输入无效！')
            else:
                #检查是否已存在同名的注册用户
                    if find(uname) > -1:
                        print('\t你输入的用户名已经使用！')
                    else:
                        pwd = input('\t请输入新用户的登陆密码：')
                        if pwd == '':
                            print('\t登陆密码无效！')
                        else:
                            userlist[index].update(uname,pwd)
                            print('\n\t已成功修改用户！')
    input('\n\t按Enter键继续……\n')
    ##函数check_update()代码结束

##函数adduser()添加新用户######################################################
def adduser():
    global userlist
    uname = input('\t请输入新的用户名：')
    if uname == '':
        print('\t该用户名输入无效！')
    else:
        #检查是否已经存在同名的注册用户
        if find(uname) > -1:
            print('\t你输入的用户名已经使用，请重新添加用户！')
        else:
            pwd = input('\t请输入新用户登陆密码：')
            if pwd =='':
                print('\t登入密码输入无效！')
            else:
                userlist.append(user(uname,pwd))
                print('\t已成功添加用户!')
    input('\n\t按Enter键继续……')
    ##函数adduser()代码结束

##函数find(namekey)查找是否存在用户名为namekey的注册用户###########################
def find(namekey):
    global userlist
    #如果注册用户列表userlist中存在namekey值同名的用户，返回位置，否则返回-1
    n = -1
    for x in userlist:
        n += 1
        if x.uname == namekey:
            break
    else:
        n = -1
    return n
    #函数find(namekey)代码结束

##函数save()将当前用户信息写入文件永久保存#################################
def save():
    global userlist
    #将用户信息写入文件永久保存
    myfile = open(r'userdata.bin','wb')
    global userlist
    dump(userlist,myfile)
    myfile.close()
    print('\t已成功保存用户信息')
    input('\n\t按Enter键继续……')
    ##函数save()代码结束

#程序启动时，载入文件中的用户信息
myfile = open(r'userdata.txt','rd')
x = myfile.read(1)          #读一个字节，检查文件是否为空
if x == b'':
    userlist = list()
else:
    myfile.seek(0)
    userlist = load(myfile)
myfile.close()

#以死循环显示系统操作菜单，直到选择退出系统
while True:
    print('用户注册信息管理系统')
    print('\t1.显示全部已注册用户')
    print('\t2.查找、修改、删除用户信息')
    print('\t3.添加新用户')
    print('\t4.保存用户数据')
    print('\t5.退出系统')
    no = input('请输入序号选择对应菜单：')
    if no == '1':
        showall()
    elif no == '2':
        check_update()
    elif no == '3':
        adduser()
    elif no == '4':
        save()
    elif no == '5':
        print('谢谢使用，系统已退出')
        break
