from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600


rad = 300 

def circle_points(x,y,cx,cy):
    
    glVertex2f(x+cx,y+cy)
    glVertex2f(y+cx,x+cy)
    
    
    glVertex2f(y+cx,-x+cy)
    glVertex2f(x+cx,-y+cy)
    
    glVertex2f(-x+cx,-y+cy)
    glVertex2f(-y+cx,-x+cy)
    
    glVertex2f(-y+cx,x+cy)
    glVertex2f(-x+cx,y+cy)
    

def mid_circle(cx,cy,radius):
    d = 1-radius
   
    x=0
    y= radius 
    circle_points(x,y,cx,cy)
    while (x<y):
        if d<0 :
            #choose E
            d  = d + 2*x + 3
        else : 
            d = d + 2*x - 2*y + 5
            y = y-1
        x= x+1
        circle_points(x,y,cx,cy)
            
            
    
    




def initialize():
    
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, WINDOW_WIDTH, 0.0, WINDOW_HEIGHT, 0, 1.0)

    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    
    glColor3f(0.447, 1.0, 0.973) 
    glPointSize(2)
    glBegin(GL_POINTS)
    mid_circle(300,300,rad)
    glEnd()
    
    
    glutSwapBuffers()
    
    
def keyboard_ordinary_keys(key,_,__):
  glutPostRedisplay()

def keyboard_special_keys(key,_,__):
    glutPostRedisplay()
    
def mouse_click(button,state,x,y):
    glutPostRedisplay()
    
def animation():
    global rad
    rad = rad
    glutPostRedisplay()    
    
def mouse_click(button, state, x, y): # handle mouse button 
    
    global rad

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        print("mouse click ",x,y)
       
    
    
       
    
    
   
        
        
        
        
glutInit()

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

glutCreateWindow(b"Assignment 3")
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutInitWindowPosition(0, 0)
glutMouseFunc(mouse_click)
glutDisplayFunc(showScreen)
# glutReshapeFunc(lambda width, height: initialize(width, height))
glutReshapeFunc(initialize())


glutKeyboardFunc(keyboard_ordinary_keys)
glutSpecialFunc(keyboard_special_keys)
glutIdleFunc(animation)
glutMainLoop()