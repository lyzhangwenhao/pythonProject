#coding=utf-8

# from docx2pdf import convert
# convert("D:/AutoExport/docx/OA测试单后遗留问题待确认9.11.docx","D:/AutoExport/pdf/OA测试单后遗留问题待确认9.11.pdf")

import os
import glob
from pathlib import Path
from docx2pdf import convert

path = 'D:/AutoExport/'
p = Path(path)
fileList = list(p.glob("**/*.docx"))
for file in fileList:
    print(file.name.split(".")[0]+".pdf")
    filename = "D:/AutoExport/pdf/" + file.name.split(".")[0]+".pdf"
    convert(file,filename)