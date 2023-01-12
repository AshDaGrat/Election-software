import xlrd
import xlwt

#xlrd boilerplate
wb = xlrd.open_workbook("usn.xls")
sheet = wb.sheet_by_index(0)
n = 3 #number of usn numbers in spreadsheet

#xlwt boilerplate


def valid_usn(m):
    for i in range(n):
        if int(sheet.cell_value(i,0)) == m:
            return True
            break
    return False
    
"""
def freeindex():
    for i in range(10000):
        if 

def addtosheet():

"""


print(valid_usn(1346))


