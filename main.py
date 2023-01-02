import sys

def getAcronymList(acronymFile):
  with open(acronymFile,"r") as f:
    lines = f.readlines()
    listOfAcronyms = []
    for line in lines:
      if "\\acro" in line.strip():
        listOfAcronyms.append(line.split("{")[1].strip("}"))
    return listOfAcronyms


#def getListOfAcronymsWithoutAc(file):
#  with open(file,"r") as f:
#    lines = f.readlines()
#    acronymsWithoutAc = []
#    for line in lines:
#      for word in line.split(" "):
#        
#    
#    return acronymsWithoutAc  

def main():
  if len(sys.argv) != 3:
    print("Usage: python main.py fileToCheck acronymFile")
    sys.exit(-1)
  print(getAcronymList(sys.argv[2]))

if __name__ == "__main__":
  main()