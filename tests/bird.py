from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import sin , cos , radians

theta = 0
side = 30
state = 1
dist = .25
max_theta = 60

def update(input):
	global theta
	global state
	global max_theta
	#dist = dist + 0.05
	if state == 1:
		theta += 1
		if theta >= max_theta:
			state = 2
	else:
		theta -= .5
		if theta <= -max_theta:
			state = 1
	glutPostRedisplay()
	glutTimerFunc(int(1000/60),update,0)

	


def drawBrid():
	global side
	global theta
	global dist
	glClear(GL_COLOR_BUFFER_BIT)
	glTranslatef(0 ,dist,0)
	glBegin(GL_LINES)
	glVertex2f(0,0)
	glVertex2f(side/2,.866*side)
	
	glVertex2f(0,0)
	glVertex2f(-side/2 , 0.866*side)
	
	glVertex2f(side/2,0.866*side)
	glVertex2f(side/2 + side*cos(radians(theta)) ,0.866*side*sin(radians(theta))+0.866*side)
	
	glVertex2f(-side/2,0.866*side)
	glVertex2f(-side/2 - side*cos(radians(theta)) ,0.866*side*sin(radians(theta))+0.866*side)
	glEnd()
	glFlush()

if __name__ == "__main__":
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB , GLUT_SINGLE)
	glutInitWindowPosition(0 , 0)
	glutInitWindowSize(500 , 500)
	glutCreateWindow("Bird Flying")
	glutDisplayFunc(drawBrid)
	glutTimerFunc(1000,update,0)
	gluOrtho2D(-100,100,-100,100)
	glutMainLoop()
