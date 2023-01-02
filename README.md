# Latex Acronym Checker

The [Acronym](https://ctan.org/pkg/acronym?lang=en "acronym") package is very useful to easily create references to the acronyms used in the document and place them as a clickable link to a glossary. 

To create an acronym one of the `ac` commands can be used; the most common `ac` command's syntax is:

```
\ac{AC_NAME}
```

, where `AC_NAME` refers to the acronym itself.

Often, however, an acronym or two are missed and, for a hulking document, it gets tiring to carefully read the whole document just to find the missing acronym; even still, it is very hard to even know if there is an acronym missing.

This script parses the whole document and finds all instances of missing acronyms and displays them on screen, alongside the line number and a visual indicator where the acronym is. 


## Disclaimer

This script was made for my own use and, although tested, may cause unwanted behavior for some people. Use at your own risk.

## Run the acronym checker

Clone the project if it is not cloned already:

```bash
git clone git@github.com:DuarteArribas/LatexAcronymChecker.git
```

Alternatively, download the zip and unzip it.

Go to the project directory:

```bash
cd LatexAcronymChecker
```

Run it as:

```bash
python main.py fileToCheck acronymFileToCheck
```

The `fileToCheck` is the path to the file to check.
The `acronymFileToCheck` is the path to the acronym file to check.

The following is a sample output from a file which contained two missing acronyms at the same line:

```
==============================================================
 There are 2 acronyms not marked as acronyms in the document.
==============================================================


== Acronym 'TCP' on line '6' ==============================
The \textit{application layer} is the topmost layer of both the \ac{OSI} and TCP/IP models and also the topmost layer of the hybrid model presented in this book.

                                                                             ^
                                                                             |
== Acronym 'IP' on line '6' ==============================
The \textit{application layer} is the topmost layer of both the \ac{OSI} and TCP/IP models and also the topmost layer of the hybrid model presented in this book.

                                                                                 ^
                                                                                 |
```