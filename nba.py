import xlrd


myFile = ("nba-data.xlsx")
wb = xlrd.open_workbook(myFile)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
mia_player = []
rows = sheet.nrows
print((sheet.cell_value(1, 1)))
if sheet.cell_value(1, 1) == "Mia":
    print("yes")
s = "Mia"
print(type(s))

for i in range(1, rows):
    if sheet.cell_value(i, 1) == "Mia":
        mia_player.append(sheet.cell_value(i, 0))
print(mia_player)

