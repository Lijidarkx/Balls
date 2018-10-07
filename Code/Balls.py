from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


class Ball3D:
	def __init__(self):
		self.balls = []
		self.width = 600
		self.height = 600
		self.window = 0
		self.depth = -10
		self.G = 0.0005
		self.V = -0.001

	def init_gl(self):
		glClearColor(0.3, 0.3, 0.3, 0.0)
		glClearDepth(1.0)
		glDepthFunc(GL_LESS)
		glEnable(GL_DEPTH_TEST)
		glPolygonMode(GL_FRONT, GL_FILL)
		glPolygonMode(GL_BACK, GL_FILL)
		glShadeModel(GL_SMOOTH)

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()

		gluPerspective(45.0, float(self.width) / float(self.height), 0.1, 100.0)

		glMatrixMode(GL_MODELVIEW)

		# glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1, 1, 1, 1])
		# glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [1, 1, 1, 1])
		# glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, [50])
		# glLightfv(GL_LIGHT0, GL_POSITION, [0.1, 0.1, -0.5, 0.5])
		# glLightfv(GL_LIGHT0, GL_AMBIENT, [0, 0, 0, 1])
		# glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])
		# glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 1, 1, 1])
		# glEnable(GL_LIGHTING)
		# glEnable(GL_LIGHT0)
		# glEnable(GL_COLOR_MATERIAL)

	def display_func(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		self.balls_show()
		self.wells_show()
		glutSwapBuffers()

	def idle_func(self):
		self.display_func()

	def balls_show(self):
		for ball in self.balls:
			glPushMatrix()
			glTranslate(ball[0][0], ball[0][1], ball[0][2])
			glColor3f(ball[2][0], ball[2][1], ball[2][2])
			glutSolidSphere(0.005, 20, 20)
			glPopMatrix()

	@staticmethod
	def wells_show():
		glColor3f(1.0, 1.0, 0.0)
		glBegin(GL_POLYGON)
		glVertex3f(-0.1, -0.1, -0.5)
		glVertex3f(0.1, -0.1, -0.5)
		glVertex3f(0.1, 0.1, -0.5)
		glVertex3f(-0.1, 0.1, -0.5)
		glEnd()

		glColor3f(0.8, 0.5, 0.0)
		glBegin(GL_POLYGON)
		glVertex3f(0.1, -0.1, -0.5)
		glVertex3f(0.1, 0.1, -0.5)
		glVertex3f(0.1, 0.1, -0.2)
		glVertex3f(0.1, -0.1, -0.2)
		glEnd()

		glColor3f(0.8, 0.5, 0.0)
		glBegin(GL_POLYGON)
		glVertex3f(-0.1, 0.1, -0.5)
		glVertex3f(-0.1, -0.1, -0.5)
		glVertex3f(-0.1, -0.1, -0.2)
		glVertex3f(-0.1, 0.1, -0.2)
		glEnd()

		glColor3f(1.0, 0.5, 0.0)
		glBegin(GL_POLYGON)
		glVertex3f(-0.1, -0.1, -0.5)
		glVertex3f(0.1, -0.1, -0.5)
		glVertex3f(0.1, -0.1, -0.2)
		glVertex3f(-0.1, -0.1, -0.2)
		glEnd()

		glColor3f(1.0, 0.5, 0.0)
		glBegin(GL_POLYGON)
		glVertex3f(0.1, 0.1, -0.5)
		glVertex3f(-0.1, 0.1, -0.5)
		glVertex3f(-0.1, 0.1, -0.2)
		glVertex3f(0.1, 0.1, -0.2)
		glEnd()

	@staticmethod
	def keyboard_func(*args):
		if args[0] == b"\x1b":
			exit()
		print(args[0])

	def mouse_func(self, *args):
		if args[0] == 0 and args[1] == 1:
			x, y, _ = gluUnProject(args[2], args[3], -0.1)
			self.balls.append([[x, -y, -0.1], [random.randint(-10, 10)/1000, 0.0, self.V], (random.randint(0, 10)/10, random.randint(0, 10)/10, random.randint(0, 10)/10)])
			print(x, y)
		print(args)

	def timer_func(self, id):
		del_list = []
		for ball in self.balls:
			#print(ball)
			if ball[0][0] < -0.1 or ball[0][0] > 0.1:
				ball[1][0] = -ball[1][0]
			if ball[0][1] < -0.1 or ball[0][1] > 0.1:
				ball[1][1] = -ball[1][1]-self.G
			if ball[0][2] < -0.5:
				ball[1][2] = -ball[1][2]
			if ball[0][2] > 0.0:
				del_list.append(self.balls.index(ball))
			for i in range(3):
				ball[0][i] += ball[1][i]
			ball[1][1] -= self.G
		for i in del_list:
			self.balls.pop(i)
		glutTimerFunc(30, self.timer_func, 1)

	def reshape_func(self, *args):
		glutReshapeWindow(self.width, self.height)

	def run(self):
		glutInit()
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
		glutInitWindowSize(self.width, self.height)
		glutInitWindowPosition(0, 0)
		self.window = glutCreateWindow(b"Balls")
		glutDisplayFunc(self.display_func)
		glutIdleFunc(self.idle_func)
		glutReshapeFunc(self.reshape_func)
		glutKeyboardFunc(self.keyboard_func)
		glutMouseFunc(self.mouse_func)
		glutTimerFunc(30, self.timer_func, 1)
		self.init_gl()
		glutMainLoop()


if __name__ == '__main__':
	main = Ball3D()
	print("Press esc to exit")
	main.run()
