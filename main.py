import sys


def main():
  if len(sys.argv) != 2:
    print("Usage: python main.py fileToCheck")
    sys.exit(-1)
  print(sys.argv[1])
  #print(getListOfAcronymsWithoutAc(sys.argv[1]))

if __name__ == "__main__":
  main()