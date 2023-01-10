from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

BIRD_CENTRE = [200,0]
BIRD_WIDTH = 75	
SPEED = 1
HEAD_RADIUS = 15
theta = 30

def init():
	glutInit()
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(500,500)
	glutCreateWindow("Flying Bird")
	glClearColor(0,0,0,0)
	gluOrtho2D(-200,200,-200,200)

def head():
	global HEAD_RADIUS
	glColor3f(1,1,1)
	glBegin(GL_POLYGON)
	vertices = [
		[(BIRD_CENTRE[0] - (BIRD_WIDTH / 2)), 10],
		[(BIRD_CENTRE[0] - (BIRD_WIDTH / 2)), -10],
		[BIRD_CENTRE[0]	- (BIRD_WIDTH), BIRD_CENTRE[1]]
	]
	for vertice in vertices:
		glVertex2fv(vertice)
	glEnd()
	glColor3f(1,1,1)
	glBegin(GL_TRIANGLE_FAN)	
	for i in range (0,361):
		x = 5 * cos(radians(i)) + (BIRD_CENTRE[0] - (BIRD_WIDTH - 7))
		y = 5 * sin(radians(i)) + BIRD_CENTRE[1]
		glVertex2f(x,y)
	glEnd()
	
def animator(x):
	global BIRD_CENTRE, SPEED, BIRD_WIDTH, theta
	BIRD_CENTRE[0] -= 0.2	
	theta += 1 * SPEED
	if theta == 0:
		SPEED = 1
	if theta >= 60:
		SPEED = -1 
	glutTimerFunc(int(1000/60), animator,0)
	glutPostRedisplay()
	
def wings():
	global theta, BIRD_CENTRE
	glColor3f(1,1,1)
	glLineWidth(5)
	glBegin(GL_LINES)
	glVertex2f(BIRD_CENTRE[0] - 10, BIRD_CENTRE[1])
	x = BIRD_CENTRE[0] + (30 * cos(radians(theta)) )
	y = BIRD_CENTRE[1] + (30 * sin(radians(theta)) )
	glVertex2f(x,y)
	glEnd()
	
	glColor3f(1,1,1)
	glLineWidth(5)
	glBegin(GL_LINES)
	glVertex2f(BIRD_CENTRE[0] - 10, BIRD_CENTRE[1])
	glVertex2f(x,-y)
	glEnd()
	
def bird():
	global BIRD_CENTRE, BIRD_WIDTH
	glColor3f(1,1,1)
	glLineWidth(3)
	glBegin(GL_LINES)
	glVertex2f(BIRD_CENTRE[0]-(BIRD_WIDTH/2), BIRD_CENTRE[1])
	glVertex2f(BIRD_CENTRE[0]+(BIRD_WIDTH/2), BIRD_CENTRE[1])
	glEnd()
	head()
	wings()
		
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	bird()
	glFlush()	
	
def main():
	init()
	glutDisplayFunc(display)
	glutTimerFunc(0,animator,0)
	glutMainLoop()

main()	