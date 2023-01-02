import sys


def main():
  if __name__ == "__main__":
    if len(sys.argv) != 1:
      print("Usage: python main.py fileToCheck")
      sys.exit(-1)
    
    print(getListOfAcronymsWithoutAc())
    