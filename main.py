import sys
from read_pgm import read_pgm
from display import display

if __name__ == "__main__":
  if (len(sys.argv) == 2):
    image = read_pgm(sys.argv[1], byteorder='>')
    display(image)

