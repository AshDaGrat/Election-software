import xlrd
import openpyxl


def valid_usn(usn, file):

    """
    Takes two parameters, USN number, and the path to the .xls file
    NEEDS TO BE .XLS FILE TYPE. CANNOT BE .XLSX TYPE
    Returns True if USN is in the first column of the first sheet of the file

    USECAGE : 
    valid_usn(12345, "data\\usn.xls") 
    >>> True
    """

    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    
    for i in range(sheet.ncols):
        if int(sheet.cell_value(i,0)) == int(usn):
            return True
    return False


def add_to_excel(num, file_path):

    """
    Takes two parameters, USN number, and the path to the .xlsx file
    NEEDS TO BE .XLSX FILE TYPE. CANNOT BE .XLS TYPE
    adds usn to first empty row in first column of sheet

    USEAGE : 
    add_to_excel(1234, "data\\done.xlsx")
    """

    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    a = sheet.max_row + 1
    cell = sheet.cell(row = a, column=1)
    cell.value = num
    # Save the changes to the workbook
    wb.save(file_path)