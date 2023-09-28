import xlrd

senders_file = xlrd.open_workbook("./assets/xls/50-pcs-2020-16.6.xlsx") 
senders_list = senders_file.sheet_by_index(0)
number_of_senders = senders_list.nrows

for i in range(0, number_of_senders):
    with open("./assets/50-pcs-2020-16.6.txt", "a", encoding="utf-8") as gmails:
        gmails.write(senders_list.cell_value(i, 0).strip() + "," + senders_list.cell_value(i, 1).strip() + "," + senders_list.cell_value(i, 2).strip() + "\n")
