from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math
from math import sin,cos,radians

year = 0
day = 0

def init(): 
   glClearColor (0.0, 0.0, 0.0, 0.0)
   glShadeModel (GL_FLAT)


def display():

   global day, year

   glClear (GL_COLOR_BUFFER_BIT)

   glColor3f (1.0, 1.0, 0, 1)
   glPushMatrix()
   glutSolidSphere(1.0, 25, 16)   # draw sun

   glRotatef(year, 0.0, 1.0, 0.0)
   year = (year + 1) % 360

   glPushMatrix()
   glTranslatef(2.0, 0.0, 0.0)
   glRotatef(day, 0.0, 1.0, 0.0)
   day = (day + 1) % 360

   glColor3f (0, 0, 1.0);
   glutWireSphere(0.2, 10, 8)    # draw smaller planet
   glPopMatrix()

   glPushMatrix()
   glTranslatef(4.0, 0.0, 0.0)
   glRotatef(day, 0.0, 1.0, 0.0)
   glColor3f (1, 0, 0.0, 1)
   glutWireSphere(0.2, 10, 8)
   glPopMatrix()

   glPopMatrix()
   glutSwapBuffers()

   # delay
   for i in range(100000):
      pass

def reshape(w, h):
   glViewport (0, 0, w, h)
   glMatrixMode (GL_PROJECTION)
   glLoadIdentity ()
   gluPerspective(70.0, w/h, 1.0, 20.0)
   glMatrixMode(GL_MODELVIEW)
   glLoadIdentity()
   gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 800)
glutInitWindowPosition (500, 500)
glutCreateWindow("Transformation | Christo Reji Sam")
init ()
glutDisplayFunc(display)
glutIdleFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()