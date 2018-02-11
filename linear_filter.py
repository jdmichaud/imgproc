import numpy as np
from scipy import signal

def blur(image):
  return signal.convolve2d(image, np.divide(
    [
      [1, 1, 1],
      [1, 2, 1],
      [1, 1, 1]
    ], 10))

def sharpen(image):
  return signal.convolve2d(image,
    [
      [-1, -1, -1],
      [-1,  9, -1],
      [-1, -1, -1]
    ])

def gaussian(image):
  return signal.convolve2d(image, np.divide(
    [
      [1,  4,  6,  4, 1],
      [4, 16, 24, 16, 4],
      [6, 24, 36, 24, 6],
      [4, 16, 24, 16, 4],
      [1,  4,  6,  4, 1],
    ], 256))

def central_difference(image):
  xdiff = np.divide([
    [ 0, 0, 0],
    [-1, 0, 1],
    [ 0, 0, 0],
  ], 2)
  ydiff = np.divide([
    [0,-1, 0],
    [0, 0, 0],
    [0, 1, 0],
  ], 2)
  return np.power(
    np.power(signal.convolve2d(image, xdiff), 2) +
    np.power(signal.convolve2d(image, ydiff), 2), 0.5
  )
