import numpy as np

def slope_intercept(image, slope, intercept):
  return np.add(np.multiply(image, slope), intercept);

def wwwl(image, ww, wl):
  low = wl - ww / 2.0
  high = wl + ww / 2.0
  # Clamp the image
  tmp = np.clip(image, low, high)
  # (x - (wl - 0.5)) / (ww) + 0.5
  return np.add(np.divide(np.subtract(tmp, wl - 0.5), ww), 0.5)
