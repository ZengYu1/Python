#coding=gbk

import sys
from math import pi as PI
from math import sin, cos
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class MyPyOpenGLTest:
    #��д���캯������ʼ��OpenGL������ָ����ʾģʽ�Լ����ڻ�ͼ�ĺ���
    def __init__(self, width=640, height=480, title='MyOpenGLTest'.encode('gbk')):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_DEPTH)
        glutInitWindowSize(width, height)
        self.window=glutCreateWindow(title)
        #ָ�����ƺ���
        glutDisplayFunc(self.Draw)
        glutIdleFunc(self.Draw)
        self.InitGL(width,height)

    #�����ض���Ҫ����һ�����OpenGL�ĳ�ʼ��
    def InitGL(self,width,height):
        #��ʼ�����ڱ���Ϊ��ɫ
        glClearColor(1.0,1.0,1.0,1.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        #�⻬��Ⱦ
        glEnable(GL_BLEND)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_POINT_SMOOTH)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_POLYGON_SMOOTH)
        glEnable(GL_PROJECTION)
        #��������Ҳ��Ϊ�����
        glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        glHint(GL_POINT_SMOOTH_HINT, GL_FASTEST)
        glLoadIdentity()
        #͸��ͶӰ�任
        gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    #�����Լ��Ļ�ͼ����
    def Draw(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        #ƽ��
        glTranslated(-3.0, 2.0, -8.0)
        #���ƶ�άģ�ͣ�z����Ϊ0
        #����ģʽ�����ƶ����
        glBegin(GL_POLYGON)
        #���ƶ�����ɫ
        glColor3f(1.0, 0.0, 0.0)
        #���ƶ���ζ���
        glVertex3f(0.0, 1.0, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, 0.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-1.0, -1.0, 0.0)
        #�������λ���
        glEnd()

        glTranslatef(3, -1, 0.0)

        #������ά�߶�
        glBegin(GL_LINES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(1.0, 1.0, -1.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, 3.0)
        glEnd()

        glTranslatef(-0.3, -1.0, 3.0)

        #ʹ�����߶λ���Բ
        glBegin(GL_LINE_LOOP)
        n = 100
        theta = 2 * PI / n
        r = 0.8
        for i in range(100):
            x = r * cos(i * theta)
            y = r * sin(i * theta)
            glVertex3f(x, y, 0)
        glEnd()

        glutSwapBuffers()

    #��Ϣ��ѭ��
    def MainLoop(self):
        glutMainLoop()



if __name__ == '__main__':
    #ʵ�������ڶ������г���������Ϣ��ѭ��
    w=MyPyOpenGLTest()
    w.MainLoop()
