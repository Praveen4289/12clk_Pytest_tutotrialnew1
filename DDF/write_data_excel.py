import openpyxl

excel_Path='C:\\Users\\pc\\Desktop\\DDF.xlsx'
wb=openpyxl.load_workbook(excel_Path)
sh=wb["Sheet2"]
for r in range(1,11):
    for c in range(1,3):
        sh.cell(row=r,column=c).value='Pytest'

wb.save(excel_Path)
print("written successfully")