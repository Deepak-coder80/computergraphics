from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

sys.setrecursionlimit(10**6)

window = 700
title = "Flood Fill"
old_color=[0,1,0]

def refresh2D(width,height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,width,0,height,0,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def getPixel(x,y):
    color = glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT)
    return color[0][0]

def ploatPixel(x,y):
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()

def flood_fill(x,y,new_color,old_color):
    color = getPixel(x,y)
    
    if all(color==old_color):
        glColor3f(new_color[0],new_color[1],new_color[2])
        ploatPixel(x,y)
        flood_fill(x+1,y,new_color,old_color)
        flood_fill(x-1,y,new_color,old_color)
        flood_fill(x,y+1,new_color,old_color)
        flood_fill(x,y-1,new_color,old_color)
        flood_fill(x+1,y+1,new_color,old_color)
        flood_fill(x-1,y-1,new_color,old_color)
        flood_fill(x-1,y+1,new_color,old_color)
        flood_fill(x+1,y-1,new_color,old_color)

def rectangle():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    refresh2D(window,window)
    glLoadIdentity()
    glColor3f(old_color[0],old_color[1],old_color[2])
    glBegin(GL_QUADS)
    glVertex2f(100,100)
    glVertex2f(500,100)
    
    glVertex2f(100,200)
    glVertex2f(500,200)
    glEnd()
    glutSwapBuffers()

def mouse(btn,state,x,y):
    
    if btn == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            
            new_color=[1,1,0]
            
            flood_fill(x,window-y,new_color,old_color)

def main():
    glutInit(sys.argv)
    glutInitWindowSize(window,window)
    glutCreateWindow(title)
    glutDisplayFunc(rectangle)
    glutMouseFunc(mouse)
    glutMainLoop()

main()