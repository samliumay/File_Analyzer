# File_Analyzer
## Explanation
- This Analyzer will able to find all the spesific PII instances.

## Current skills of the program
- Currenlty the program is able to find the mails in the spesific document.
- .txt, .xls, .csv, .pdf is accapted as input.
-  Will return the number of mails that is available in the document.

## Future skills of the program 
- Will able to detect all the Pll's at the future.
- Will have an interface.
- Will be an exe version of platform with and without an interface.

## How to use?
### Way 1
-Firstly clone the project.
```
git clone https://github.com/samliumay/File_Analyzer.git
python main.py
```
-Then enter the document path.
Example:
```
Hello, Please enter the file location
File location:C:\Users\Desktop\example.txt
```
### Way2
```
Will be available at the future
```

### Notes and Warnings
- Be aware of that you need to install the spesific packages before using the code. All the packages should be installed. 
```
import os
import re
import PyPDF2
import docx
import openpyxl
```
You can install the packages with 
```
pip install (a package that you need)
```
