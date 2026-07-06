from openpyxl import load_workbook

workbook = load_workbook("data/model_v14.xlsx")

sheet = workbook.active

print(sheet["A2"].value)
print(sheet["B2"].value)