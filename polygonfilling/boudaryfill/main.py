from OpenGL.GL import *
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import sys

sys.setrecursionlimit(10**6)

def refresh2D(width,height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-100,width,-100,height,0,-1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def bound_it( x, y, fill, bg):
    color=[0,0,0]
    glReadPixels(x,450-y,1.0,1.0,GL_RGB,GL_FLOAT,color)

    if(
        (color[0]!=bg[0] or color[1]!=bg[1] or color[2]!=bg[2])
        and (color[0]!=fill[0] or color[1]!=fill[1] or color[2]!=fill[2])
    ):

        glColor3f(fill[0],fill[1],fill[2])
        glPointSize(10)
       
        glBegin(GL_POINTS)
        glVertex2f(x,450-y)
        glEnd()
        glFlush()
        bound_it(x+1,y,fill,bg)
        bound_it(x-2,y,fill,bg)
        bound_it(x,y+2,fill,bg)
        bound_it(x,y-2,fill,bg)



def mouse(btn ,state,x,y):
    
    if(btn==GLUT_LEFT_BUTTON):
        if(state==GLUT_UP):
            print(x,y)
            bCol=[1,0,0]
            color=[0,0,1]
            bound_it(x,450-y,bCol,color)
    
  


def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    refresh2D(500,500)
    glLoadIdentity()
    glLineWidth(3)
    glPointSize(2)
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(150,100)
    glVertex2f(300,300)
    glVertex2f(450,100)
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