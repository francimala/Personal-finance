import gspread
import os
import json
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

#IMPORTANT: if you are going to use it in Pietra Ligure you have to change "Francesco" with "User"
JSON_FILENAME = 'C:/Users/Francesco/Google Drive/Documenti/Conoscenza personale/Python/Personal_finance_google_sheet/Personal finance-c9cd69e27773.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_FILENAME, scope)

gc = gspread.authorize(credentials) #We need to authorize the access to our Google Spreadsheet
wks = gc.open('Spese personali').sheet1 #We need to create a variable to save the Google Spreadsheet

money_comma = [] #In this list we are going to save every value with google numer's format (16,00 i.e.)
money_str = []
money_float = [] #This list contains the same values of money_comma, but stored as float

#We need to set 12 variables to 2 since each value starts from second row
jan = 2
feb = 2
mar = 2
apr = 2
may = 2
jun = 2
jul = 2
aug = 2
sep = 2
oct = 2
nov = 2
dec = 2

total_month = [0]*12

#We are now going to read every column
dates_list = wks.col_values(1)
money_list = wks.col_values(3)

#Now we need to delate the first two rows because there are no values in them
real_money_list = money_list[2:]
print(real_money_list)
real_dates_list = dates_list[2:]
print(real_dates_list)

#We are now taking all money from the list in google spreadsheet.
#Google save every value with '€' before numbers, we need to delate it in order to use them
for i in real_money_list:
    i.split()
    money_comma.append(i.split()[1])
#print(money_comma)

#We are now delating all commas from all values in money_comma, in order to convert them in float:
#we read all list until the comma, we add a point and then we continue
#with the rest of the list (numbers)
for i in money_comma:
    if len(i) == 5:
        money_str.append(i[:2] + '.' + i[3:])
    elif len(i) == 4:
        money_str.append(i[:1] + '.' + i[2:])
    elif len(i) == 6:
        money_str.append(i[:3] + '.' + i[4:])

#Now we need to create a new list made of float
for d in money_str:
    money_float.append(float(d))

#print(money_float)

#We want to store every data in the corret column (the correct month), so we simply need to check
#the second element of the list in 'real_dates_list'
for j, k in zip(real_dates_list, money_float):

    if j.split('/')[1] == '01':
        total_month[0] += k
        jan += 1

    if j.split('/')[1] == '02':
        total_month[1] += k
        feb += 1

    if j.split('/')[1] == '03':
        total_month[2] += k
        mar += 1

    if j.split('/')[1] == '04':
        total_month[3] += k
        apr += 1

    if j.split('/')[1] == '05':
        total_month[4] += k
        may += 1

    if j.split('/')[1] == '06':
        total_month[5] += k
        jun += 1

    if j.split('/')[1] == '07':
        total_month[6] += k
        jul += 1

    if j.split('/')[1] == '08':
        total_month[7] += k
        aug += 1

    if j.split('/')[1] == '09':
        total_month[8] += k
        sep += 1

    if j.split('/')[1] == '10':
        total_month[9] += k
        oct += 1

    if j.split('/')[1] == '11':
        total_month[10] += k
        nov += 1

    if j.split('/')[1] == '12':
        total_month[11] += k
        dec += 1

#Now we need to update every column
for h in range(12):
    wks.update_cell(2, h + 6, total_month[h])
