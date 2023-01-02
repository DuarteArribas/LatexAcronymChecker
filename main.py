import sys

def getAcronymList(acronymFile):
  with open(acronymFile,"r") as f:
    lines = f.readlines()
    listOfAcronyms = []
    for line in lines:
      if "\\acro" in line.strip():
        listOfAcronyms.append(line.split("{")[1].strip("}"))
    return listOfAcronyms


def getListOfAcronymsWithoutAc(file,acronyms):
  with open(file,"r") as f:
    lines = f.readlines()
    acronymsWithoutAc = []
    lineCount = 1
    for line in lines:
      for word in line.split(" "):
        for acronym in acronyms:
          if acronym in word:
            if all([acronymPrefix not in word for acronymPrefix in ["\\ac","\\Ac"]]) and "\\label" not in word and line.strip()[0] != "%":
              acronymsWithoutAc.append((acronym,lineCount,line))
      lineCount += 1
    return acronymsWithoutAc
    
def printListOfAcronymsWithoutAc(acronymsWithoutAc):
  if len(acronymsWithoutAc):
    print(f"There are {len(acronymsWithoutAc)} acronyms not marked as acronyms in the document.")
  else:
    print(f"All the acronyms are marked. Good Job!")
    return
  print("\n\n")
  for acronymWithoutAc in acronymsWithoutAc:
    print(f"| Acronym '{acronymWithoutAc[0]}' on line {acronymWithoutAc[1]} |\n{acronymWithoutAc[2]}")
    print(" " * acronymWithoutAc[2].index(acronymWithoutAc[0]),end='')
    print("^")
    print(" " * acronymWithoutAc[2].index(acronymWithoutAc[0]),end='')
    print("|")

def main():
  if len(sys.argv) != 3:
    print("Usage: python main.py fileToCheck acronymFile")
    sys.exit(-1)
  acronymsWithoutAc = getListOfAcronymsWithoutAc(sys.argv[1],getAcronymList(sys.argv[2]))
  printListOfAcronymsWithoutAc(acronymsWithoutAc)

if __name__ == "__main__":
  main()