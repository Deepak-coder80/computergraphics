from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import *

r1 = 40
r2 = 130 
xt = 300                            #x reference point
yt = 0                              #y reference point
speed = 1                           #angle incrementing factor
theta = 0

ax = []
ay = []
def init():
 glutInit()
 glutInitDisplayMode(GLUT_RGB)
 glutInitWindowSize(500,500)
 glutCreateWindow("Bouncing ball")
 glClearColor(0.0,0.0,0.0,0.0)
 gluOrtho2D(-500,500,-500,500)
 
def circle():                       #function to plot circle
 global r1,r2,xt,yt,theta
 
 xc = r2*cos(radians(theta)) + xt   #position of circle w.r.t to new refernce point xt
 yc = r2*sin(radians(theta)) + yt   #position of circle w.r.t to new refernce point yt
 
 glColor3f(1.0,1.0,0.0)
 glPointSize(3.0)
 glBegin(GL_POINTS)                 #plotting circle using polar algorithm
 #for j in range (0,r1):
 for i in range (0,46):
  x = r1*cos(radians(i))
  y = r1*sin(radians(i))   
  glVertex2f(x+xc,y+yc)
  glVertex2f(x+xc,-y+yc)
  glVertex2f(-x+xc,y+yc)
  glVertex2f(-x+xc,-y+yc)
  glVertex2f(y+xc,x+yc)
  glVertex2f(y+xc,-x+yc)
  glVertex2f(-y+xc,x+yc)
  glVertex2f(-y+xc,-x+yc)
  ax.append(xc)                     #appending current x position of centre of circle to plot the ball trail to an array
  ay.append(yc)                     #appending current y position of centre of circle to plot trail to an array
 glEnd()

 
def trail():                        #function to plot the trail
 global ax,ay
 glColor3f(1,1,1)
 glPointSize(1)
 glBegin(GL_POINTS)
 for i in range (0,len(ax)):        #plotting trail
  glVertex2f(ax[i],ay[i])
 glEnd()

def update(n):	                    #function to animate the circle and trail
 global r1,r2,xt,yt,speed,theta
 theta += speed                     #angle being updated
 if theta == 0:                      
  speed = -speed
 elif theta == 181:                 #theta gets updated 0 on reaching 180
  theta = 0
  xt -= (2*r2-30)                   #reference point xt is updated 
  r2 -= 30                          #radius being updated
  
 if r2 < 0 or r2 == 0:
  speed = 0                         #ball is made to stop
  
 glutTimerFunc(int(1000/60),update,0)
 glutPostRedisplay()
 
def display():                      #display function
 glClear(GL_COLOR_BUFFER_BIT)
 trail()
 circle()
 glFlush()
 
def main():
 init()
 glutDisplayFunc(display)
 glutTimerFunc(0,update,0)
 glutMainLoop()
 
main()