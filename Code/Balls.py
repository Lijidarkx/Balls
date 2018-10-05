from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

window = 0
rtri = 0.0
rquad = 2.0
speed = 0.1
Wireframe = True
balls = []


def InitGL(Width, Height):
	glClearColor(0.3, 0.3, 0.3, 0.0)
	glClearDepth(1.0)
	glDepthFunc(GL_LESS)
	glEnable(GL_DEPTH_TEST)
	glPolygonMode(GL_FRONT, GL_FILL)
	glPolygonMode(GL_BACK, GL_FILL)
	glShadeModel(GL_SMOOTH)

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

	gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)

	glMatrixMode(GL_MODELVIEW)

	glMaterialfv(GL_FRONT, GL_SPECULAR, [1, 1, 1, 1])
	glMaterialfv(GL_FRONT, GL_SHININESS, [50])
	glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 1, 0])
	glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 0, 1])
	glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 1, 0, 1])
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.1, 0.1, 0.1, 1.0])
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)


def ReSizeGLScene(Width, Height):
	if Height == 0:
		Height = 1

	glViewport(0, 0, Width, Height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
	glMatrixMode(GL_MODELVIEW)




def DrawGLScene():
	global rtri, rquad, speed, balls

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	#for ball in balls:

	glTranslatef(0.0, 0.0, -10.0)
	glutSolidSphere(1.0, 50, 50)
	glTranslatef(5.0, 0.0, 0.0)
	glutSolidSphere(1.0, 50, 50)
	glTranslatef(-10.0, 0.0, 0.0)
	glutSolidSphere(1.0, 50, 50)

	rtri = rtri + 0.2
	rquad = rquad - 0.15
	glutSwapBuffers()


def keyPressed(*args):
	global rquad
	if args[0] == b"x":
		global Wireframe
		if Wireframe == False:
			glPolygonMode(GL_FRONT, GL_LINE)
			glPolygonMode(GL_BACK, GL_LINE)
			Wireframe = True
		elif Wireframe == True:
			glPolygonMode(GL_FRONT, GL_FILL)
			glPolygonMode(GL_BACK, GL_FILL)
			Wireframe = False
		else:
			pass
	elif args[0] == b"\x1b":
		exit()
	elif args[0] == b"v":
		rquad = 2
		print(rquad)

	print(args[0])


def mousePressed(*args):
	if args[0] == 0 and args[1] == 1:
		global balls
		balls.append((args[2], args[3]))


def main():
	global window
	glutInit()
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutInitWindowSize(800, 500)
	glutInitWindowPosition(0, 0)
	window = glutCreateWindow(b"Balls")
	glutDisplayFunc(DrawGLScene)
	glutIdleFunc(DrawGLScene)
	glutReshapeFunc(ReSizeGLScene)
	glutKeyboardFunc(keyPressed)
	glutMouseFunc(mousePressed)
	InitGL(640, 480)
	glutMainLoop()


print("Press esc to exit")
main()
