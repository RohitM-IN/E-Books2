import wget
import xlrd

loc = ("Springer Ebooks-converted.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
sheet.cell_value(0, 0)

for i in range(sheet.nrows):
    data = sheet.row_values(i)
    url = data[0]
    name = data[1]
    print('\nBeginning', name, 'download with wget module')
    wget.download(url, name)
