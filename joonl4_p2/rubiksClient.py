problem_name = 'rubiks'

def client_mainloop():
  print(TITLE)
  #print(PROBLEM.PROBLEM_NAME + "; " + PROBLEM.PROBLEM_VERSION)
  global STEP, DEPTH, OPERATORS, CURRENT_STATE, STATE_STACK
  CURRENT_STATE = PROBLEM.copy_state(PROBLEM.INITIAL_STATE)  

  STATE_STACK = [CURRENT_STATE]
  STEP = 0
  DEPTH = 0
  PROBLEM.render_state(CURRENT_STATE)
  while(True):
    #print("\nStep "+str(STEP)+", Depth "+str(DEPTH))
    #print("CURRENT_STATE = \n"+ str(CURRENT_STATE))
    if PROBLEM.goal_test(CURRENT_STATE):
      print('''CONGRATULATIONS!
You have solved the problem by reaching a goal state.
Do you wish to continue exploring?
''')
      answer = input("Y or N? >> ")
      if answer=="Y" or answer=="y": print("OK, continue")
      else: return

    applicability_vector = get_applicability_vector(CURRENT_STATE)
    #print("applicability_vector = "+str(applicability_vector))
    for i in range(len(OPERATORS)):
      if applicability_vector[i]:
        print(str(i) + ": " + OPERATORS[i].name)
    command = input("Enter command: 0, 1, 2, etc. for operator; H-help; Q-quit. >> ")

    if command=="H" or command=="h": show_instructions(); continue
    if command=="Q" or command=="q": break
    if command=="": continue
    try:
      i = int(command)
    except:
      print("Unknown command or bad operator number.")
      continue
    print("Operator " + str(i) + " selected.")
    if i<0 or i>= len(OPERATORS):
      print("There is no operator with number " + str(i))
      continue
    if applicability_vector[i]:
       CURRENT_STATE = OPERATORS[i].apply(CURRENT_STATE)
       STATE_STACK.append(CURRENT_STATE)
       PROBLEM.render_state(CURRENT_STATE)
       DEPTH += 1
       STEP += 1
       continue
    else:
       print("Operator " + str(i) +" is not applicable to the current state.")
       continue
    #print("Operator "+command+" not yet supported.")

def get_applicability_vector(s):
    #print("OPERATORS: "+str(OPERATORS))
    return OPERATORS

def exit_client():
  print("Terminating Text_SOLUZION_Client session.")
  log("Exiting")
  exit()
  

def show_instructions():
  print('''\nINSTRUCTIONS:\n
Welcome to the virtual Rubik's cube! Each face of the cube is represented
by a 3x3 square. The square in the middle of the cross is the front face. 
The squares on either side of the middle are the left and right faces. 
The squares above and below the middle are the top and bottom faces. Finally,
the square on the far right is the back face. Each time you make a move, the 
colors on the faces will change respectively. Note that due to display limitations,
the back face appears as if you are facing it, so the tiles may seem reversed.
Your goal is to arrive at a point in which each face has a unique color.

The current state of your problem session represents where you
are in the problem-solving process.  You can try to progress
forward by applying an operator to change the state.
To do this, type the number of an applicable operator.
The program shows you a list of what operators are 
applicable in the current state. If you reach the goal state, you have solved the problem, and the 
system will tell you. Good luck and have fun!
''')
      
def apply_one_op():
    """Populate a popup menu with the names of currently applicable
       operators, and let the user choose which one to apply."""
    currently_applicable_ops = applicable_ops(CURRENT_STATE)
    #print "Applicable operators: ",\
    #    map(lambda o: o.name, currently_applicable_ops)
    print("Now need to apply the op")

def applicable_ops(s):
    """Returns the subset of OPERATORS whose preconditions are
       satisfied by the state s."""
    return OPERATORS

import sys, importlib.util

# Get the PROBLEM name from the command-line arguments

if len(sys.argv)<2:
  """ The following few lines go with the LINUX version of the text client.
  print('''
       Usage: 
./IDLE_Text_SOLUZION_Client <PROBLEM NAME>
       For example:
./IDLE_Text_SOLUZION_Client Missionaries
  ''')
  exit(1)
  """
  sys.argv = ['rubiksClient.py', problem_name] # IDLE and Tk version only.
  # Sets up sys.argv as if it were coming in on a Linux command line.
  
problem_name = sys.argv[1]
print("problem_name = " + problem_name)

try:
  spec = importlib.util.spec_from_file_location(problem_name, problem_name+".py")
  PROBLEM = spec.loader.load_module()
  spec.loader.exec_module(PROBLEM)
except Exception as e:
  print(e)
  exit(1)

print("ABOUT TO IMPORT")
try:
  spec = importlib.util.spec_from_file_location(problem_name+'_Array_VIS_FOR_TK',
                                                problem_name+'_Array_VIS_FOR_TK.py')
  VIS = spec.loader.load_module()
  spec.loader.exec_module(VIS)
  print("Using TK vis routine")
  PROBLEM.render_state = VIS.render_state
  VIS.initialize_vis()
except Exception as e:
  print(e)
  exit(1)


OPERATORS=PROBLEM.OPERATORS
STATE_STACK = []
TITLE="rubiksClient"

import threading
class Client(threading.Thread):
  def __init__(self, tk_root):
    self.root = tk_root
    threading.Thread.__init__(self)
    self.start()

  def run(self):
    client_mainloop()
    self.root.quit()
    exit(0)
    #self.root.update()
  
# The following is only executed if this module is being run as the main
# program, rather than imported from another one.
if __name__ == '__main__':
  import show_state_array
  client = Client(show_state_array.STATE_WINDOW)
  show_state_array.STATE_WINDOW.mainloop()
  print("The session is finished.")