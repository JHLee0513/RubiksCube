from show_state_array import initialize_tk, state_array, state_display, STATE_WINDOW, test

from tkinter import font

from rubiks import describe_state

myFont=None

WIDTH = 650
HEIGHT = 500
TITLE = 'Rubik\'s Cube'

def initialize_vis():
  initialize_tk(WIDTH, HEIGHT, TITLE)
  
def render_state(s):
    s = describe_state(s)
    # Note that font creation is only allowed after the Tk root has been
    # defined.  So we check here if the font creation is still needed,
    # and we do it (the first time this method is called).
    global myFont
    if not myFont:
        myFont = font.Font(family="Helvetica", size=18, weight="bold")
    print("In render_state, state is\n" + str(s))
    print()
    # Create the default array of colors
    white = (255,255,255)
    yellow = (255,255,0)
    red = (255,0,0)
    orange = (255,128,0)
    green = (0,255,0)
    blue = (0,0,255)
    gray = (128,128,128) #background

    #Now create the default array of string labels
    row = [gray]*12
    the_color_array= [row, row[:], row[:], row[:], row[:], row[:], row[:], row[:],row[:]]
    #Adjust colors and strings to match the state
    for row in range(0,9):
      for column in range(0,12):
        if s[row][column] == 0:
          the_color_array[row][column] = red
        elif s[row][column] == 1:
          the_color_array[row][column] = green
        elif s[row][column] == 2:
          the_color_array[row][column] = orange
        elif s[row][column] == 3:
          the_color_array[row][column] = blue
        elif s[row][column] == 4:
          the_color_array[row][column] = white
        elif s[row][column] == 5:
          the_color_array[row][column] = yellow
        else:
          the_color_array[row][column] = gray
      
    the_state_array = state_array(color_array=the_color_array)
    the_state_array.show()