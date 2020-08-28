#coding=utf-8
import xlrd
rd = xlrd.open_workbook("C:/Users/Mi_dad/Desktop/机组1部件1测点1.xls")

print('sheet数量：',rd.nsheets)
print('sheet名称',rd.sheet_names())

sh1 = rd.sheet_by_index(0)
print("sheet %s 共%d行 %d列"%(sh1.name,sh1.nrows,sh1.ncols))
print("第三行第一列数据：",sh1.cell_value(2,2))
