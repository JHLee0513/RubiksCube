'''
rubiksCube.py
(Rubik's Cube Problem)
A SOLUZION problem formulation.
'''

import numpy as np
from random import randint

#<METADATA>
SOLUZION_VERSION = "1.0"
PROBLEM_NAME = "Rubik's cube"
PROBLEM_VERSION = "1.4"
PROBLEM_AUTHORS = ['Brian Lee, Caelen Wang']
PROBLEM_CREATION_DATE = "31-AUG-2017"
PROBLEM_DESC=\
'''
"Rubik's Cube is a 3-D combination puzzle
invented in 1974 by Hungarian sculptor and
professor of architecture Ernő Rubik."
- wikipedia
'''
#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>

#<COMMON_CODE>
def copy_state(s):
	return s[:]

def move(olds,direction,layer,choice):
	'''This method computes
	the new state resulting
	from moving the chosen
	side of the cube.'''

	#olds refers to current state, which will be a list of matrices
	#direction can be either horizontal or vertical
	#layer refers to which of the layer will be moved
	#choice refers to the direction the layer will be moved in

	s = copy_state(olds)
	s0 = s[0] #front
	s1 = s[1] #left
	s2 = s[2] #back
	s3 = s[3] #right
	s4 = s[4] #top
	s5 = s[5] #bottom

	if direction == 'hori':
		if layer == 'top':
			if choice == 'left':
				cero = list(s0[0,:])
				uno = list(s1[0,:])
				dos = list(s2[0,:])
				tres = list(s3[0,:])

				s0[0,:] = tres
				s1[0,:] = cero
				s2[0,:] = uno
				s3[0,:] = dos
				
				s4 = np.rot90(s4,3)
				new_state = [s0, s1, s2, s3, s4, s5]
		
			elif choice == 'right':
				cero = list(s0[0,:])
				uno = list(s1[0,:])
				dos = list(s2[0,:])
				tres = list(s3[0,:])

				s0[0,:] = uno
				s1[0,:] = dos
				s2[0,:] = tres
				s3[0,:] = cero
				
				s4 = np.rot90(s4,1)
				new_state = [s0, s1, s2, s3, s4, s5]
		
		elif layer == 'bot':
			if choice == 'left':
				cero = list(s0[2,:])
				uno = list(s1[2,:])
				dos = list(s2[2,:])
				tres = list(s3[2,:])

				s0[2,:] = tres
				s1[2,:] = cero
				s2[2,:] = uno
				s3[2,:] = dos
				
				s5 = np.rot90(s5,1)
				new_state = [s0, s1, s2, s3, s4, s5]
			elif choice == 'right':
				cero = list(s0[2,:])
				uno = list(s1[2,:])
				dos = list(s2[2,:])
				tres = list(s3[2,:])

				s0[2,:] = uno
				s1[2,:] = dos
				s2[2,:] = tres
				s3[2,:] = cero
				
				s5 = np.rot90(s5,3)
				new_state = [s0, s1, s2, s3, s4, s5]
		
		elif layer == 'all':
			if choice == 'left':
				cero = s0[:]
				uno = s1[:]
				dos = s2[:]
				tres = s3[:]

				s0 = tres
				s1 = cero
				s2 = uno
				s3 = dos
				
				s4 = np.rot90(s4,3)
				s5 = np.rot90(s5,1)
				new_state = [s0, s1, s2, s3, s4, s5]

			elif choice == 'right':
				cero = s0[:]
				uno = s1[:]
				dos = s2[:]
				tres = s3[:]

				s0 = uno
				s1 = dos
				s2 = tres
				s3 = cero
				
				s4 = np.rot90(s4,1)
				s5 = np.rot90(s5,3)
				new_state = [s0, s1, s2, s3, s4, s5]
		
	  
	elif direction == 'vert':
		if layer == 'left':
			if choice == 'up':
				cero = list(s0[:,0])
				quatro = list(s4[:,0])
				dos = list(s2[:,2])
				cinco = list(s5[:,0])

				s0[:,0] = cinco
				s4[:,0] = cero
				s2[:,2] = quatro
				s5[:,0] = dos

				s1 = np.rot90(s1,1)
				new_state = [s0, s1, s2, s3, s4, s5]
		
			elif choice == 'down':
				cero = list(s0[:,0])
				quatro = list(s4[:,0])
				dos = list(s2[:,2])
				cinco = list(s5[:,0])

				s0[:,0] = quatro
				s4[:,0] = dos
				s2[:,2] = cinco
				s5[:,0] = cero

				s1 = np.rot90(s1,3)
				new_state = [s0, s1, s2, s3, s4, s5]
		
		elif layer == 'right':
			if choice == 'up':
				cero = list(s0[:,2])
				quatro = list(s4[:,2])
				dos = list(s2[:,0])
				cinco = list(s5[:,2])

				s0[:,2] = cinco
				s4[:,2] = cero
				s2[:,0] = quatro
				s5[:,2] = dos

				s3 = np.rot90(s3,3)
				new_state = [s0, s1, s2, s3, s4, s5]
		
			elif choice == 'down':
				cero = list(s0[:,2])
				quatro = list(s4[:,2])
				dos = list(s2[:,0])
				cinco = list(s5[:,2])

				s0[:,2] = quatro
				s4[:,2] = dos
				s2[:,0] = cinco
				s5[:,2] = cero

				s3 = np.rot90(s3,1)
				new_state = [s0, s1, s2, s3, s4, s5]
		
	return new_state

def describe_state(s):
	# Produces a textual description of a state.
	# Might not be needed in normal operation with GUIs.
	copy = copy_state(s)
	s0 = copy[0]
	s1 = copy[1]
	s2 = copy[2]
	s3 = copy[3]
	s4 = copy[4]
	s5 = copy[5]

	zero = np.array([[999,999,999],[999,999,999],[999,999,999]])

	sideA = np.concatenate((zero, s4, zero, zero), axis = 1)
	sideB = np.concatenate((s1, s0, s3, s2), axis = 1)
	sideC = np.concatenate((zero, s5, zero, zero), axis = 1)

	txt = np.concatenate((sideA, sideB, sideC), axis = 0)
	return txt

class Operator:
	def __init__(self, name, state_transfer):
		self.name = name
		self.state_transfer = state_transfer

	def apply(self, s):
		return self.state_transfer(s)
#</COMMON_CODE>

#<OPERATORS>
DLC_combinations = [('hori','top','left'), ('hori','top','right'), ('hori','bot','left'), ('hori','bot','right'), ('hori','all','left'),\
			('hori','all','right'), ('vert','left','up'), ('vert','left','down'), ('vert','right','up'), ('vert','right','down')]

OPERATORS = [Operator(\
	"Turn " + l + " layer " + c + ".",\
	lambda s, d1=d, l1=l, c1=c: move(s,d1,l1,c1))\
	for (d,l,c) in DLC_combinations]
#</OPERATORS>

#<MORE COMMON CODE>
#returns complete face
def new_face(n):
	return np.array([[n,n,n],[n,n,n],[n,n,n]])

#returns scrambled state
def scramble():
	state = [new_face(0),new_face(1),new_face(2),new_face(3),new_face(4),new_face(5)]
	for i in range(50):
		combo = DLC_combinations[randint(0,9)]
		state = move(state,combo[0],combo[1],combo[2])
	return state

#tests if a face is complete
def is_complete(face):
	return (face[0,0]==face[0,1] and face[0,0]==face[0,2]\
		and face[0,0]==face[1,0] and face[0,0]==face[1,1] and face[0,0]==face[1,2]\
		and face[0,0]==face[2,0] and face[0,0]==face[2,1] and face[0,0]==face[2,2])

#tests if the cube is solved
def goal_test(s):
  p = s[:]
  return (is_complete(p[0]) and is_complete(p[1]) and is_complete(p[2]) and is_complete(p[3]) and is_complete(p[4]) and is_complete(p[5]))

def goal_message(s):
  return "Congratulations on successfully solving the Rubik's cube!"
#</MORE COMMON CODE

#<INITIAL_STATE>
INITIAL_STATE = scramble()
#INITIAL_STATE = [new_face(0),new_face(1),new_face(2),new_face(3),new_face(4),new_face(5)]
#</INITIAL_STATE>

#<GOAL_TEST> 
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> 
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

#<STATE_VIS>
render_state = None
  
def use_BRIFL_SVG():
  global render_state
  from rubiksCube_SVG_VIS_FOR_BRIFL import render_state
#</STATE_VIS>

# s = INITIAL_STATE[:]

# while(True):
# 	print(describe_state(s))
# 	i = int(input("""0 - turn top layer left
# 1 - turn top layer right					
# 2 - turn bottom layer left
# 3 - turn bottom layer right
# 4 - rotate cube left by one face
# 5 - rotate cube right by one face
# 6 - turn left layer up
# 7 - turn left layer down
# 8 - turn right layer up
# 9 - turn right layer down
# 404 - Quit
# Choose an option: """))
# 	if(i==404): 
# 		print("Goodbye")
# 		break

# 	s = OPERATORS[i].state_transfer(s)
# 	#print(s)