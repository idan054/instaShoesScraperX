# Sources:
# https://github.com/burnash/gspread
# https://docs.gspread.org/en/latest/
# https://pypi.org/project/gspread/

import gspread

gc = gspread.service_account(filename="../cerdi.json")

sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/12xTW6jLIQ1yx538eo3bQ1veDd8zhItJ3oImINvOEaUE/edit?usp=sharing')
# sh = gc.open_by_key('12xTW6jLIQ1yx538eo3bQ1veDd8zhItJ3oImINvOEaUE')

# Most common case: Sheet1
worksheet = sh.sheet1

# all_col_values_lists = worksheet.get_all_values()
# print(*all_col_values_lists, sep="\n")

# Get next empty row
colA_values = worksheet.col_values(1)
empty_row = len(colA_values)+1

# Update a range
worksheet.update(f'A{empty_row}:Z{empty_row}', [
    ["A", "B"],
])