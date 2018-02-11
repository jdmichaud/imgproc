import numpy as np
from scipy import signal

def blur(image):
  return signal.convolve2d(image, np.divide(
    [
      [1, 1, 1],
      [1, 2, 1],
      [1, 1, 1]
    ], 10), mode='same')

def sharpen(image):
  return signal.convolve2d(image,
    [
      [-1, -1, -1],
      [-1,  9, -1],
      [-1, -1, -1]
    ], mode='same')

def gaussian(image):
  return signal.convolve2d(image, np.divide(
    [
      [1,  4,  6,  4, 1],
      [4, 16, 24, 16, 4],
      [6, 24, 36, 24, 6],
      [4, 16, 24, 16, 4],
      [1,  4,  6,  4, 1],
    ], 256), mode='same')

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
    np.power(signal.convolve2d(image, xdiff, mode='same'), 2) +
    np.power(signal.convolve2d(image, ydiff, mode='same'), 2), 0.5
  )

def sobel(image):
  # Horizontal edges
  h1 = [
    [ 1,  2,  1],
    [ 0,  0,  0],
    [-1, -2, -1],
  ]
  # Diagonal edges
  h2 = [
    [ 0,  1, 2],
    [-1,  0, 1],
    [-2, -1, 0],
  ]
  # Vertical edges
  h3 = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1],
  ]
  return np.power(
    np.power(signal.convolve2d(image, h1, mode='same'), 2) +
    np.power(signal.convolve2d(image, h2, mode='same'), 2) +
    np.power(signal.convolve2d(image, h3, mode='same'), 2), 0.5
  )

def unsharpen(image, blurfactor=1):
  return np.subtract(image, np.multiply(blur(image), blurfactor))
