from OpenGL.GL import *
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import sys
import numpy as np

sys.setrecursionlimit(10**6)

def refresh2D(width,height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,width,0,height,0,-1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def read_pixel(x,y):
    color = glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT)
    return color[0][0]
    #return np.array([round(x) for x in color[0][0]])

def ploat_pixel(x,y):
   
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()

def bound_it( x, y, fill, bg):
    color = read_pixel(x,y)
    
    # fill = np.array(fill)
    # bg = np.array(bg)
    if(not all(color==fill)and not all(color==bg)):
            glColor3f(fill[0],fill[1],fill[2])
            ploat_pixel(x,y)
            bound_it(x+1,y,fill,bg)
            bound_it(x-1,y,fill,bg)
            bound_it(x,y+1,fill,bg)
            bound_it(x,y-1,fill,bg)
            bound_it(x+1,y+1,fill,bg)
            bound_it(x-1,y+1,fill,bg)
            bound_it(x+1,y-1,fill,bg)
            bound_it(x-1,y-1,fill,bg)
            
            
   

def mouse(btn ,state,x,y):    
    if(btn==GLUT_LEFT_BUTTON):
        if(state==GLUT_DOWN):
            bCol=[1,0,0]
            color=[0,1,1]
            bound_it(x,500-y,color,bCol)
    
  


def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    refresh2D(500,500)
    glLoadIdentity()
    glLineWidth(3)
    glPointSize(2)
    glColor3f(1,0,0)
    glBegin(GL_LINES)
    glVertex2f(150,100)
    glVertex2f(300,300)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(300,300)
    glVertex2f(450,100)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(450,100)
    glVertex2f(150,100)
    glEnd()
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(500,500)
    glutCreateWindow("BOUNDARY FILL")
    glutDisplayFunc(draw)
    glutMouseFunc(mouse)
    glutMainLoop()

main()