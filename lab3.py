from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
rad = 0
speed = 0.05
paused = False

circles = []


class Circle:
    def __init__(self, cx, cy, radius):
        self.cx = cx
        self.cy = cy
        self.radius = radius

    def draw(self):
        glBegin(GL_POINTS)
        mid_circle(self.cx, self.cy, self.radius)
        glEnd()

    def grow(self):
        self.radius +=speed


def circle_Points(x, y, cx, cy):
    glVertex2f(x + cx, y + cy)
    glVertex2f(y + cx, x + cy)

    glVertex2f(y + cx, -x + cy)
    glVertex2f(x + cx, -y + cy)

    glVertex2f(-x + cx, -y + cy)
    glVertex2f(-y + cx, -x + cy)

    glVertex2f(-y + cx, x + cy)
    glVertex2f(-x + cx, y + cy)


def mid_circle(cx, cy, radius):
    d = 1 - radius
    x = 0
    y = radius

    circle_Points(x, y, cx, cy)

    while x < y:
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * x - 2 * y + 5
            y = y - 1
        x = x + 1
        circle_Points(x, y, cx, cy)


def initialize():
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, WINDOW_WIDTH, 0.0, WINDOW_HEIGHT, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0.447, 1.0, 0.973)
    glPointSize(2)

    for circle in circles:
        circle.draw()
                                        # circle rendering hoy
    glutSwapBuffers()



def animation():
    global rad, paused, circles
    if not paused:
        # Create a new list to store circles to be removed
        circles_to_remove = []

        for circle in circles:
            circle.grow()

            a = (0, 0)
            b = (600, 0)
            c = (0, 600)
            d = (600, 600)

            # Calculate distance to each corner
            dist_to_a = math.dist((circle.cx, circle.cy), a)
            dist_to_b = math.dist((circle.cx, circle.cy), b)
            dist_to_c = math.dist((circle.cx, circle.cy), c)
            dist_to_d = math.dist((circle.cx, circle.cy), d)

            # Calculate maximum distance to any corner
            max_dist = max(dist_to_a, dist_to_b, dist_to_c, dist_to_d)

            if max_dist <= circle.radius: #max distance circle theke choto hoye gele
                print("removing")
                circles_to_remove.append(circle)

        # Remove circles outside the loop
        for circle in circles_to_remove:
            circles.remove(circle)

        glutPostRedisplay()





def mouse_callback(button, state, x, y):
    global rad

    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN and not paused: #circle append hoy
        new_circle = Circle(x, WINDOW_HEIGHT - y, 0)
        circles.append(new_circle)


def keyboard_callback(key, x, y):
    global paused, speed

    if key == b' ':
        paused = not paused
    

def keyboard_special_keys(key, x, y):
    global speed,paused
    if not paused:
        if key == GLUT_KEY_LEFT: # Decrease speed
            speed = max(speed - 0.1, 0.01)
        elif key == GLUT_KEY_RIGHT: # Increase speed 
            speed +=0.1

    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutInitWindowPosition(0, 0)

wind = glutCreateWindow(b"Growing Circles")
glutDisplayFunc(showScreen)
glutIdleFunc(animation)
glutMouseFunc(mouse_callback)
glutKeyboardFunc(keyboard_callback)
glutSpecialFunc(keyboard_special_keys)
initialize()
glutMainLoop()
