from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 800, 600 #window size
raindrop_spacing = 40
raindrop_size = 10  # raindrop size as small line
raindrop_speed = 0.5
background_color = [0.0, 0.0, 0.0]  # black
direction = -1  # Raindrops fall downward

#2D point
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y =y

raindrop_columns = []  #raindrop store  [[point(x,y).......],]

def draw_rain():
    glColor3f(0.0, 0.0, 1.0) #blue
    for column in raindrop_columns:
        glBegin(GL_LINES)  # Draw raindrops as lines
        for drop in column:
            #raindrop er line er vertex
            glVertex2f(drop.x, drop.y)  #start
            glVertex2f(drop.x, drop.y - raindrop_size) #end
        glEnd()

def generate_raindrops():
    global raindrop_columns
    raindrop_columns = []
    num_columns = int(W_Width / raindrop_spacing) # calculate kortesi koyta coloum possible
    for i in range(num_columns):
        column = [] #raindrop position store korbo
        for j in range(W_Height, 0, -raindrop_spacing): #top to bottom with also calculte spacing
            x = i * raindrop_spacing + random.randint(-10, 10)
            y = j + random.randint(-10, 10)
            column.append(Point(x, y))
        raindrop_columns.append(column)
    return raindrop_columns

horizontal_direction = 0

def animate():
    global raindrop_columns
    for column in raindrop_columns: #[(x,y),(x,y)]
        for drop in column: #(x,y)
            drop.x +=horizontal_direction  # left right bend
            drop.y -= raindrop_speed  # Raindrops fall vertically
            if drop.y < 0:
                drop.y = W_Height  # Reset raindrop's vertical position when it goes out of the window
            if drop.x > W_Width or drop.x < 0:
                drop.x = random.randint(0, W_Width)  # Reset raindrop's horizontal position when it goes out of the window
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global horizontal_direction
    if key == GLUT_KEY_RIGHT:
        horizontal_direction += 1  #horizontal direction to right 
    elif key == GLUT_KEY_LEFT:
        horizontal_direction -= 1  #horizontal direction to left 
    else:
        horizontal_direction = 0  # Reset horizontal direction if any other key is pressed
    glutPostRedisplay()



def draw_background():
    glClearColor(background_color[0], background_color[1], background_color[2], 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

def keyboardListener(key, x, y):
    #global direction
    global background_color
    if key == b'q':
        exit(0)
    elif key == b'n' or key == b'N':  
        background_color = [0.0, 0.0, 0.0]  # Night (black) background
    elif key == b'd' or key == b'D':  
        background_color = [1.0, 1.0, 1.0]  # Day (white) background
    glutPostRedisplay()


def init():
    glMatrixMode(GL_PROJECTION) #3D ke 2D te convert
    glLoadIdentity() #reset
    gluOrtho2D(0, W_Width, 0, W_Height)

def display():
    draw_background()
    draw_rain()
    draw_house()  # Call the function to draw the house
    glutSwapBuffers()

def draw_house():
    
    glColor3f(1.0, 0.0, 0.0)  
    glBegin(GL_TRIANGLES)
    glVertex2f(400, 550)  # Roof top
    glVertex2f(220, 400)  # Bottom left corner
    glVertex2f(620, 400)  # Bottom right corner
    glEnd()

    glColor3f(1.0, 1.0, 0.0)  # Yellow color for the body
    glBegin(GL_TRIANGLES)
    glVertex2f(220, 400)  # Bottom left corner
    glVertex2f(620, 400)  # Bottom right corner
    glVertex2f(620, 200)  # Top right corner

    glVertex2f(620, 200)  # Top right corner
    glVertex2f(220, 200)  # Top left corner
    glVertex2f(220, 400)  # Bottom left corner
    glEnd()

   
    glColor3f(0.0, 1.0, 0.0) 
    glBegin(GL_TRIANGLES)
    glVertex2f(340, 200)  # Bottom left corner
    glVertex2f(480, 200)  # Bottom right corner
    glVertex2f(480, 350)  # Top right corner

    glVertex2f(480, 350)  # Top right corner
    glVertex2f(340, 350)  # Top left corner
    glVertex2f(340, 200)  # Bottom left corner
    glEnd()

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"TASK 1: Rainy House Simulation")
init()
raindrop_columns = generate_raindrops()
glutDisplayFunc(display)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutIdleFunc(animate)
glutMainLoop()


