import sys
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#global variables
WIDTH, HEIGHT = 800, 600
points = []
speed = 0.5
frozen = False
blinking = False

def draw_point(x, y, color, size=10):
    glColor3f(color[0], color[1], color[2]) #color
    glPointSize(size) #size
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def random_color():
    return random.random(), random.random(), random.random() #random RGB color

def random_direction():
    return random.choice([-1, 1]) #possible 4 combination

def point(x, y):
    direction_x = random_direction()
    direction_y = random_direction()
    original_color = random_color()  # Generate and store the original color
    color = original_color  
    return [x, y, direction_x, direction_y, color, original_color]  # Include original_color cz of blinking purpouse


def draw_points():
    for point in points:
        draw_point(point[0], point[1], point[4]) #x,y,color from the return fun of point

def mouse_button(button, state, x, y):
    global points, blinking, frozen
    if not frozen:
        if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
            y = HEIGHT - y
            points.append(point(x, y))
        elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            toggle_blink()

def keyboardListener(key, x, y):
    global speed, frozen
    if key == b'n':
        glutLeaveMainLoop()
    elif key == b' ':
        frozen = not frozen

def special_key(key, x, y):
    global speed, frozen
    if key == GLUT_KEY_UP:
        speed += 1
    elif key == GLUT_KEY_DOWN:
        speed = max(speed - 1, 0.5)

def update_points():
    global points
    if not frozen:
        for point in points:
            point[0] += point[2] * speed #x+= direction of X
            point[1] += point[3] * speed
            if point[0] <= 0 or point[0] >= WIDTH:
                point[2] *= -1 #reverse direction at edge left right
            if point[1] <= 0 or point[1] >= HEIGHT:
                point[3] *= -1 #reverse at top bottom

def display():
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT) #clear color buffer
    draw_points()
    if blinking:
        blink_points()
    glutSwapBuffers() # Swap the front and back buffers to display the rendered image

def reshape(width, height):
    global WIDTH, HEIGHT
    WIDTH, HEIGHT = width, height
    glViewport(0, 0, width, height) #cover entire window
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WIDTH, 0, HEIGHT) #  2D orthographic projection
    

def idle():
    update_points()
    glutPostRedisplay()

def toggle_blink():
    global blinking
    blinking = not blinking

def blink_points():
    global points
    if blinking:
        for point in points:
            if point[4] == (0, 0, 0):
                point[4] = point[5]
            else:
                point[4] = (0, 0, 0)



# Initialize the OpenGL environment
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Set display mode with double buffering and RGB color
glutCreateWindow(b"Interactive Points Box")  # Create the window with the specified title
glutDisplayFunc(display)  # Set the display function
glutReshapeFunc(reshape)  # Set the reshape function
glutMouseFunc(mouse_button)  # Set the mouse button function
glutKeyboardFunc(keyboardListener)  # Set the keyboard function
glutSpecialFunc(special_key)  # Set the special key function
glutIdleFunc(idle)  # Set the idle function
glutMainLoop()  # Start the main loop

