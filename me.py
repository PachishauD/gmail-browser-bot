from src.utilities.select_message_for_sending import select_random_msg, read_file_line_by_line
import xlrd, time, random


# sender = []
# senders = []
# recipients = read_file_line_by_line("./assets/txt/recipients.txt")
# recipients1 = recipients
# number_of_recipients = len(recipients)
# senders_file = xlrd.open_workbook("./assets/xls/50-pcs-2020-16.6.xlsx") 
# senders_list = senders_file.sheet_by_index(0)
# number_of_senders = senders_list.nrows
# print(recipients1)
# print(number_of_recipients, number_of_senders)
# for i in range(0, number_of_senders):
#     senders.append(i)
# number = 0
# while True:
#     number_of_recipients = len(recipients)
#     number_of_senders = len(senders)
#     number_of_loop = int(number_of_recipients / number_of_senders)
#     if number_of_recipients == 0:
#         break
#     elif number_of_recipients < number_of_senders:
#         for i in range(0, number_of_recipients):
#             random_number = random.randrange(0, number_of_recipients)
#             print(senders_list.cell_value(i, 0) + " sent to : " + recipients[random_number])
#             recipients.remove(recipients[random_number])
#             number_of_recipients = len(recipients)
#             print(number_of_recipients)
#             number += 1
#             print(number)
#     else:
#         for i in senders:
#             for j in range(0, number_of_loop):  
#                 try:
#                     email = senders_list.cell_value(i, 0)
#                     random_number = random.randrange(0, number_of_recipients)
#                     if email == "emmanuelbamaiyi9098@gmail.com" or email == "azubikeemmanuel200@gmail.com":
#                         senders.remove(i)
#                         break
#                     else:
#                         print(senders_list.cell_value(i, 0) + " sent to : " + recipients[random_number])
#                         recipients.remove(recipients[random_number])
#                         number_of_recipients = len(recipients)
#                         print(number_of_recipients)
#                 except:
#                     pass
#                 number += 1
#                 print(number)
# print("end!")
# print(senders)

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

# # Instantiate a ChromeDriver instance
# driver = webdriver.Chrome(ChromeDriverManager().install())

# # Navigate to the Gmail login page
# driver.get('https://www.gmail.com')

# # Enter your Gmail account credentials
# email_input = driver.find_element(by=By.ID, value='identifierId')
# email_input.send_keys('your_email_address')
# next_button = driver.find_element(by=By.ID, value='identifierNext')
# next_button.click()

# password_input = driver.find_element(by=By.NAME, value='password')
# password_input.send_keys('your_password')
# password_button = driver.find_element(by=By.ID, value='passwordNext')
# password_button.click()

# # Click on the profile picture icon to open the profile settings menu
# profile_picture = driver.find_element(by=By.CSS_SELECTOR, value='.gb_Ca.gbii')
# profile_picture.click()

# # Click on the "Change" button to upload a new profile picture
# change_button = driver.find_element(by=By.CSS_SELECTOR, value='.gb_Da.gbii')
# change_button.click()

# # Upload the new profile picture file
# file_input = driver.find_element(by=By.NAME, value='file')
# file_input.send_keys('/path/to/your/new/profile/picture.jpg')

# # Confirm the changes by clicking on the "Save" button
# save_button = driver.find_element(by=By.CSS_SELECTOR, value='.gb_Ea.gbii')
# save_button.click()
# l = read_file_line_by_line("./assets/gmail list usa_2.txt")
# print(len(l))
# import os

# # Get the current file's directory
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # Construct the path to the image in the assets folder
# folder_path = "./assets/profile_picture/profile_pictures"
# file_names = os.listdir(folder_path)
# image_path = os.path.join(current_dir, 'assets\profile_picture\profile_pictures', file_names[random.randrange(0, len(file_names))])

# first_name = select_random_msg("./assets/txt/female names.txt").strip().capitalize()
# last_name = select_random_msg("./assets/txt/female names.txt").strip().capitalize()

# print(first_name + " " + last_name)
# # Print the image path
# print("Image path:", image_path)
# print(len(file_names))

# x  = read_file_line_by_line("total.txt")[0]
# total = int(x) + 4
# print(total)

x = [1, 2, 3, 4, 5]
for i in range(0, 10):
    if i in x:
        continue
    else:
        x.append(i)
print(x)