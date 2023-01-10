from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
title = "Translation"
width,height = 800,700
window =0


def refresh2D(width,height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-300,width,-300,height,0,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    refresh2D(width,height)
    glLoadIdentity()
    glColor3f(0,1,0)
    glPointSize(12)
    draw_x_axis()
    draw_y_axis()
    ploat_point(100,100,150,150)
    translate_150unit(100,100,150,150,200,300)
    scale(100,100,150,150,1/4,1/4,100,100)
    rotate_45_degree(100,100,150,150,100,100)
    reflection_about_orgin(100,100,150,150)
    glutSwapBuffers()

def ploat_point(x,y,width,height):
    glBegin(GL_QUADS)
    glVertex2f(x,y)
    glVertex2f(x+width,y)
    glVertex2f(x+width,y+height)
    glVertex2f(x,y+height)
    glEnd()

def translate_150unit(x,y,width,height,tx,ty):
    glBegin(GL_QUADS)
    glVertex2f(x+tx,y+ty)
    glVertex2f(x+width+tx,y+ty)
    glVertex2f(x+width+tx,y+height+ty)
    glVertex2f(x+tx,y+height+ty)
    glEnd()

def scale(x,y,width,height,sx,sy,xr,yr):
    glBegin(GL_QUADS)
    glColor3f(1,0,0)
    glVertex2f(((x-xr)*sx)+xr,((y-yr)*sy)+yr)
    glVertex2f((((x-xr)+width)*sx)+xr,((y-yr)*sy)+yr)
    glVertex2f((((x-xr)+width)*sx)+xr,(((y-yr)+height)*sy)+yr)
    glVertex2f((x-xr)+xr,(((y-yr)+height)*sy)+yr)
    glEnd()

def new_rotate_x(x,y,theta):
    return (x*math.cos(theta)-y*math.sin(theta))

def new_rotate_y(x,y,theta):
    return (x*math.sin(theta)+y*math.cos(theta))

def rotate_45_degree(x,y,width,height,xr,yr):
    glBegin(GL_QUADS)
    glColor3f(1,1,0)
    glVertex2f(new_rotate_x(x-xr,y-yr,45)+xr,new_rotate_y(x-xr,y-yr,45)+yr)
    glVertex2f(new_rotate_x(x-xr,y-yr+width,45)+xr,new_rotate_y(x-xr,y-yr+width,45)+yr)
    glVertex2f(new_rotate_x(x-xr+height,y-yr+width,45)+xr,new_rotate_y(x-xr+height,y-yr+width,45)+yr)
    glVertex2f(new_rotate_x(x-xr+height,y-yr,45)+xr,new_rotate_y(x-xr+height,y-yr,45)+yr)
    glEnd()

def reflection_about_orgin(x,y,width,height):
    glBegin(GL_QUADS)
    glColor3f(0,1,1)
    glVertex2f(-x,-y)
    glVertex2f(-(x+width),-y)
    glVertex2f(-(x+width),-(y+height))
    glVertex2f(-x,-(y+height))
    glEnd()


def draw_x_axis():
    glBegin(GL_LINES)
    glColor3f(1,1,1)
    glVertex2f(-250,0)
    glVertex2f(580,0)
    glEnd()
    displayText(600,0,"X axis")

def draw_y_axis():
    glBegin(GL_LINES)
    glColor3f(1,1,1)
    glVertex2f(0,-250)
    glVertex2f(0,580)
    glEnd()
    displayText(0,600,"Y axis")

def displayText(x,y,text):
    glRasterPos2f(x,y)
    glColor3f(1,1,1)
    for i in range(len(text)):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(text[i]))
def main():
    glutInit(sys.argv)
    glutInitWindowPosition(0,0)
    glutInitWindowSize(width,height)
    glutCreateWindow(title)
    glutDisplayFunc(draw)
    glutMainLoop()


main()