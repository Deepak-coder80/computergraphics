from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

title="Bresenham Line Drawing"
window =0
width,height = 500,500

def refresh2D(width,height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,width,0,height,0,1)
    glLoadIdentity()

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2D(width,height)
    glColor3f(1,1,0)
    glPointSize(12)
    bresenHam(10,10,80,50)
    glutSwapBuffers()

def bresenHam(x1,y1,x2,y2):
    x=x1
    y=y1
    dx=x2-x1
    dy=y2-y1
    p = 2*dy-dx
    glBegin(GL_POINTS)
    while x<=x2:
        glVertex2f(x,y)
        x=x+1
        if p<0:
            p = p+2*dy 
        else:
            p=p+2*dy-2*dx
            y=y+1
    glEnd()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(width,height)
    glutInitWindowPosition(0,0)
    window=glutCreateWindow(title)
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()

main()