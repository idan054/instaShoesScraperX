# Sources:
# https://github.com/burnash/gspread
# https://docs.gspread.org/en/latest/
# https://pypi.org/project/gspread/

import gspread
from color_printer import printGreen, printYellow

try:
    gc = gspread.service_account(filename="../cerdi.json")
except:
    gc = gspread.service_account(filename="cerdi.json")

sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/12xTW6jLIQ1yx538eo3bQ1veDd8zhItJ3oImINvOEaUE/edit?usp=sharing')
# sh = gc.open_by_key('12xTW6jLIQ1yx538eo3bQ1veDd8zhItJ3oImINvOEaUE')

# Most common case: Sheet1
worksheet = sh.sheet1

# values_list = worksheet.col_values(1)
# print(*values_list, sep="\n")

exists_users = 0
new_users = 0
def update_nxt_row(current_username, rows_lists):
    global new_users, exists_users
    # Get A column Values
    usernames_list = worksheet.col_values(1)
    # print(*usernames_list, sep="\n")
    if current_username not in usernames_list:
        # Get next empty row
        colA_values = worksheet.col_values(1)
        empty_row = len(colA_values) + 1

        # Update a range
        worksheet.update(f'A{empty_row}:Z999', rows_lists)
        printGreen(f"GSheet Updated! - {current_username}")
        new_users += 1
        print("new users:", new_users)
    else:
        exists_users +=1
        printYellow(f"{current_username}, Probably already exist...")
        print("exist users:", exists_users)

## Example
# update_nxt_row([
#     ["Row 1", "Row 1"],
#     ["Row 2", "Row 2"]
# ])