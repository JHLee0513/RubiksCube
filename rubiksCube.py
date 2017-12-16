'''
rubiksCube.py
(Rubik's Cube Problem)
A SOLUZION problem formulation.
'''

import numpy as np

#<METADATA>
SOLUZION_VERSION = "1.0"
PROBLEM_NAME = "Rubik's cube"
PROBLEM_VERSION = "1.1"
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

def move(olds,direction,layer,choice):
  '''This method computes
     the new state resulting
     from moving the chosen
     side of the cube.'''

  #old refers to current state, which will be a list of matrices
  #layer refers to which of the layer will be moved
  #choice refers to the direction the layer will be moved in

  s = copy_state(olds)
  side1 = np.array(s[0])
  side2 = np.array(s[1])
  side3 = np.array(s[2])
  side4 = np.array(s[3])
  side5 = np.array(s[4])
  side6 = np.array(s[5])

  if direction == 'hori'
    if layer == 'top'
      if choice == 'left'
        temp = side2[0,:]
        side2[0,:] = side1[0,:]
        temp2 = side3[0,:]
        side3[0,:] = temp
        temp = side4[0,:]
        side4[0,:] = temp2
        side1[0,:] = temp
        #Above is all lateral movement
        #below is movement of top layer

        rotated = list(reversed(zip(*side5)))
        side5 = rotated
        
      elif choice == 'right'
        temp = side4[0,:]
        side4[0,:] = side1[0,:]
        temp2 = side3[0,:]
        side3[0,:] = temp
        temp = side2[0,:]
        side2[0,:] = temp2
        side1[0,:] = temp
        #Above is all lateral movement
        #below is movement of top layer
        rotated = list(reversed(zip(*side5)))
        rotated2 = list(reversed(zip(*rotated)))
        rotated3 = list(reversed(zip(*rotated2)))
        side5 = rotated3
        
    elif layer == 'bot'
      if choice == 'left'
        temp = side2[2,:]
        side2[2,:] = side1[2,:]
        temp2 = side3[2,:]
        side3[2,:] = temp
        temp = side4[2,:]
        side4[2,:] = temp2
        side1[2,:] = temp
        #Above is all lateral movement
        #below is movement of top layer
        rotated = list(reversed(zip(*side6)))
        side6 = rotated
      elif choice == 'right'
        temp = side4[2,:]
        side4[2,:] = side1[2,:]
        temp2 = side3[2,:]
        side3[2,:] = temp
        temp = side2[2,:]
        side2[2,:] = temp2
        side1[2,:] = temp
        #Above is all lateral movement
        #below is movement of top layer
        rotated = list(reversed(zip(*side6)))
        rotated2 = list(reversed(zip(*rotated)))
        rotated3 = list(reversed(zip(*rotated2)))
        side6 = rotated3
        
    elif layer == 'all'
      if choice == 'left'
        temp = side2
        side2 = side1
        temp2 = side4
        side4 = side3
        side3 = temp
        side1 = temp2
        #Above lateral
        #Below is rotation of top/bottom sides
        rotated = list(reversed(zip(*side5)))

      elif choice == 'right'
        temp = side4
        side4 = side1
        temp2 = side3
        side3 = temp
        temp = side2
        side2 = temp2
        side1 = temp
        #Above lateral
        #Below is rotation of top/bottom sides
        rotated = list(reversed(zip(*side6)))
        rotated2 = list(reversed(zip(*rotated)))
        rotated3 = list(reversed(zip(*rotated2)))
        side6 = rotated3
      
  elif direction == 'vert'
    if layer == 'left'
      if choice == 'up'
        temp = side5[:,0]
        side5[:,0] = side1[:,0]
        temp2 = side3[:,2]
        side3[:,2] = temp
        temp = side6[:,0]
        side6[:,0] = temp2
        side1[:,0] = temp
        #Above is lateral
        #Below is rotation of adjacent sides
        rotated = list(reversed(zip(*side2)))
        rotated2 = list(reversed(zip(*rotated)))
        rotated3 = list(reversed(zip(*rotated2)))
        side2 = rotated3
        
      elif choice == 'down'
        temp = side6[:,0]
        side6[:,0] = side1[:,0]
        temp2 = side3[:,2]
        side3[:,2] = temp
        temp = side5[:,0]
        side5[:,0] = temp2
        side1[:,0] = temp
        #Above is lateral movement
        #below is rotation of adjacent side
        rotated = list(reversed(zip(*side2)))
        side2 = rotated
        
    if layer == 'right'
      if choice == 'up'
        temp = side5[:,2]
        side5[:,2] = side1[:,2]
        temp2 = side3[:,]
        side3[:,0] = temp
        temp = side6[:,2]
        side6[:,2] = temp2
        side1[:,2] = temp
        #above is lateral
        #below is rotation of adjacent side
        rotated = list(reversed(zip(*side4)))
        side4 = rotated
        
      elif choice == 'down'
        temp = side6[:,2]
        side6[:,2] = side1[:,2]
        temp2 = side3[:,0]
        side3[:,0] = temp
        temp= side5[:,2]
        side5[:,2] = temp2
        side1[:,2] = temp
        #above is lateral
        #below is rotation of adjacent side
        rotated = list(reversed(zip(*side4)))
        rotated2 = list(reversed(zip(*rotated)))
        rotated3 = list(reversed(zip(*rotated2)))
        side4 = rotated3
        
  return newState


def describe_state(s):
  # Produces a textual description of a state.
  # Might not be needed in normal operation with GUIs.
  s = copy_state(olds)
  side1 = np.array(s[0])
  side2 = np.array(s[1])
  side3 = np.array(s[2])
  side4 = np.array(s[3])
  side5 = np.array(s[4])
  side6 = np.array(s[5])

  side7 = np.zeros((3,3))
  side8 = np.zeros((3,3))
  side9 = np.zeros((3,3))
  side10 = np.zeros((3,3))
  side11 = np.zeros((3,3))
  side12 = np.zeros((3,3))
  side13 = np.zeros((3,3))

  sideA = np.concatenate((side7, side5, side8, side9), axis = 1)
  sideB = np.concatenate((side2, side1, side4, side3), axis = 1)
  sideC = np.concatenate((side10, side6, side11, side12), axis = 1)

  txt = np.concatenate((sideA, sideB, sideC), axis = 0)
  return txt


