import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

title="Circle Drawing"
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

def draw(xc,yc,radius,choice):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2D(width,height)
    glColor3f(1,0,0)
    glPointSize(5)
    if choice ==1 :
        
        ploat(xc,yc,radius)
    elif choice == 2:
        ploat_polar_circle(xc,yc,radius)
    else:
        ploat_non_polar_circle(xc,yc,radius)
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

        ploat_symetric(x1,y1,x,y)           

    glEnd()

def ploat_polar_circle(x1,y1,r):
    x=x1
    y=y1
    radius = r
    theta = 0.0
    glBegin(GL_POINTS)
    while theta<=6.28:
        x=x1+radius*math.cos(theta)
        y=y1+radius*math.sin(theta)
        glVertex2f(x,y)
        theta += (1/radius)
    glEnd()

def ploat_non_polar_circle(x1,y1,r):
    x,y=x1,r 
    glBegin(GL_POINTS)
    ploat_symetric(x1,y1,x-x1,y)
    while x<(x1+r):
        x +=1
        y= math.sqrt((r*r)-((x-x1)*(x-x1)))
        ploat_symetric(x1,y1,x-x1,y)
    glEnd()

def ploat_symetric(x1,y1,x,y):
    glVertex2f(x1+x,y1+y);
    glVertex2f(x1+y,y1+x);
    glVertex2f(x1-y,y1+x);
    glVertex2f(x1-x,y1+y);
    glVertex2f(x1-x,y1-y)
    glVertex2f(x1-y,y1-x);
    glVertex2f(x1+y,y1-x);
    glVertex2f(x1+x,y1-y);   


def main():
    xc = int(input('Enter center x coordinate : '))
    yc = int(input('Enter center y coordinate : '))
    radius = int(input('Enter radius of circle : '))
    print('\n Enter 1 for midpoint circle drawing')
    print(' Enter 2 for polar circle drawing')
    print(' Enter 3 for nonpolar circle drawing')
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
    glutDisplayFunc(lambda:draw(xc,yc,radius,choice))
    glutMainLoop()

main()