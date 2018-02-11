import numpy as np
from scipy import signal

def window(image, centerx, centery, size = 3):
  ''' Given a 2D-array, returns an nxn array whose "center" element is arr[x,y]'''
  arr=np.roll(np.roll(image, shift = -centerx + 1, axis = 0), shift = -centery + 1, axis = 1)
  return arr[:size, :size]

# Very very naive implementation with a way to high complexity
def median(image, size = 3):
  p = image.tolist()
  middle = int((size * size - 1) / 2)
  for i in range(1, len(image) - 1):
    for j in range(1, len(image[0]) - 1):
      p[i][j] = sorted(window(image, i, j, size).flatten())[middle]
  return p
