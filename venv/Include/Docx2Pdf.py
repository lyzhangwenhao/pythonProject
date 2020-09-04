#coding=utf-8

from docx2pdf import convert
convert("D:/AutoExport/docx/尚硅谷大数据技术之Hadoop（HDFS） (v1.0).docx","D:/AutoExport/pdf/尚硅谷大数据技术之Hadoop（HDFS） (v1.0).pdf")

# import os
# import glob
# from pathlib import Path
# from docx2pdf import convert

# path = 'D:/AutoExport/'
# p = Path(path)
# fileList = list(p.glob("**/*.docx"))


# for file in fileList:
#     print(file.name.split(".")[0]+".pdf")
#     filename = "D:/AutoExport/pdf/" + file.name.split(".")[0]+".pdf"
#     convert(file,filename)

# for file in fileList:
#     convert(file,f"{file}.pdf")