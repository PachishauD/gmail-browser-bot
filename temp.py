from src.utilities.select_message_for_sending import read_file_line_by_line

# url_valid_accs = "./assets/100 valid account.csv"
# senders = read_file_line_by_line(url_valid_accs)
# print(len(senders))
# for i in range(0, 50):
#     email = senders[i].split(",")[0].strip()
#     password = senders[i].split(",")[1].strip()
#     recovery = senders[i].split(",")[2].strip()
#     app_password = senders[i].split(",")[3].strip()
#     backup_code1 = senders[i].split(",")[4].strip()
#     backup_code2 = senders[i].split(",")[5].strip()
#     print(email, password, recovery, app_password, backup_code1, backup_code2)

# url_gmails = "./assets/txt/list usa test for manual bcc.txt"

# all_gmails = read_file_line_by_line(url_gmails)
# num_gmails = len(all_gmails)

# for i in range(0, num_gmails):
#     if "@gmail.com" in all_gmails[i]:
#         with open("./assets/real_gmails.txt", "a", encoding="utf-8") as file:
#             file.write(all_gmails[i].strip() + "\n")

url_accs = "./assets/Dzimitry_Accounts.txt"

all_accs = read_file_line_by_line(url_accs)

num_accs = len(all_accs)
for i in range(0, num_accs):
    filename = "./assets/accs" + format(i % 16 + 1) + ".txt"
    with open(filename, "a", encoding="utf-8") as file:
        file.write(all_accs[i].strip() + "\n")
    
        