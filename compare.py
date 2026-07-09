from parser import read_excel

model_v14 = read_excel("data/model_v14.xlsx")
model_v15 = read_excel("data/model_v15.xlsx")

for field in model_v14:
    old_value = model_v14[field]["value"]
    new_value = model_v15[field]["value"]

    if old_value != new_value:
        status = "CHANGED"
    else:
        status = "UNCHANGED"

    print(field)
    print("Old", old_value)
    print("New", new_value)
    print("Status", status)
    print("-------------------")