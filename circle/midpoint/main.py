from cmath import cos,sin
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

title="Midpoint Circle Drawing"
width = 500
height = 400
window =0

def refresh2D(width,height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,width,0,height,0,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2D(width,height)
    glColor3f(1,0,0)
    glPointSize(12)
    ploat(250,250,150)
    glutSwapBuffers()

def ploat(x1,y1,radius):
    y = radius
    x=0
    p = 1.25-radius
    glBegin(GL_POINTS)
    while x<=y:
        x+=1
        if p<0:
            p=p+2*x+3
        else:
            p=p+2*(x-y)+1
            y-=1

        glVertex2f(x1+x,y1+y);
        glVertex2f(x1+y,y1+x);
        glVertex2f(x1-y,y1+x);
        glVertex2f(x1-x,y1+y);
        glVertex2f(x1-x,y1-y)
        glVertex2f(x1-y,y1-x);
        glVertex2f(x1+y,y1-x);
        glVertex2f(x1+x,y1-y);       

    glEnd()

def main():
    glutInit(sys.argv)
    glutInitWindowSize(width,height)
    glutInitWindowPosition(0,0)
    window = glutCreateWindow(title)
    glutDisplayFunc(draw)
    glutMainLoop()

main()