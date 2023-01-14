import xlrd
#import xlwt

def valid_usn(usn, file):
    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    for i in range(sheet.ncols):
        if int(sheet.cell_value(i,0)) == usn:
            return True
    return False

print(valid_usn(12345, "Election-software\\usn.xls"))