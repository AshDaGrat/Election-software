import openpyxl


def valid_usn(usn, file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    
    for i in range(1, sheet.max_row+1):
        cell = sheet.cell(row = i, column=1)
        if int(cell.value) == int(usn):
            return True
    return False


def add_to_excel(usn, file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    a = sheet.max_row + 1
    cell = sheet.cell(row = a, column=1)
    cell.value = usn
    wb.save(file_path)