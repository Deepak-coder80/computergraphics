import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

title="Elipse Drawing"
width = 700
height = 600
window =0

def refresh2D(width,height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,width,0,height,0,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw(choice):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2D(width,height)
    glColor3f(1,0,0)
    glPointSize(5)
    ploat_non_polar_elipse(250,250,100,120)
    glutSwapBuffers()


def ploat_polar_elipse(xc,yc,rx,ry):

    theta = 0.0
    glBegin(GL_POINTS)
    while theta<=1.57:
        x=rx*math.cos(theta)
        y=ry*math.sin(theta)
        ploat_symetric(xc,yc,x,y)
        theta += 0.001
    glEnd()

def ploat_non_polar_elipse(xc,yc,rx,ry):
    x=0
    glBegin(GL_POINTS)
    
    while x<=rx:        
        y= ry *(math.sqrt(1-((x/rx)*(x/rx))))
        x +=0.01
        ploat_symetric(xc,yc,x,y)
    glEnd()

def ploat_symetric(x1,y1,x,y):
    glVertex2f(x1+x,y1+y);
    glVertex2f(x1+x,y1-y);  
    glVertex2f(x1-x,y1+y);
    glVertex2f(x1-x,y1-y);   


def main():
    # xc = int(input('Enter center x coordinate : '))
    # yc = int(input('Enter center y coordinate : '))
    # radius = int(input('Enter radius of circle : '))
    # print('\n Enter 1 for midpoint circle drawing')
    # print(' Enter 2 for polar circle drawing')
    # print(' Enter 3 for nonpolar circle drawing')
    choice = int(input('\nEnter your choice here : '))
    glutInit(sys.argv)
    glutInitWindowSize(width,height)
    glutInitWindowPosition(0,0)
    if choice ==1 : 
        title = 'midpoint circle drawing'
    elif choice == 2:
        title = 'polar circle drawing'
    else : 
        title = 'nonpolar circle drawing'
        
    window = glutCreateWindow(title)
    glutDisplayFunc(lambda:draw(choice))
    glutMainLoop()

main()