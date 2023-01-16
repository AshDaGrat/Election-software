import xlrd
import xlwt

def valid_usn(usn, file):

    """
    Takes two parameters, USN number, and the path to the .xls file
    NEEDS TO BE .XLS FILE TYPE. CANNOT BE .XLSX TYPE
    Returns True if USN is in the first column of the first sheet of the file

    USECASE : 
    valid_usn(12345, "Election-software\\data\\usn.xls") 
    >>> True
    """

    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    for i in range(sheet.ncols):
        if int(sheet.cell_value(i,0)) == int(usn):
            return True
    return False

def add_to_sheet(usn, file):
    """
    TODO
    1. open sheet as per path
    2. find the first free index in the first column
    3. add usn as int type to that index
    """