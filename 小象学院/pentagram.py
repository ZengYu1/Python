# coding=utf-8
"""
    作者：曾雨
    功能：五角星的绘制
    版本：1.0
    日期：01/09/2018
"""
import turtle

def main():
    """
    主函数
    """
    pass
    count = 1
    while count <= 5:
        turtle.forward(300)
        turtle.right(180-36)
        count += 1
    turtle.exitonclick()


if __name__ == '__main__':
    main()