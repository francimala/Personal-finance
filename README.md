# Personal finance organization
Hey there, this is a simple python project I'm currently using to organize my personal finance starting from a simple Google Spreadsheet weekly updated. The idea is based on the video published by the YouTube channel PrettyPrinted that you can find here: https://www.youtube.com/watch?v=7I2s81TsCnc&list=PLXL_6wK-bGzeDvfMMBEQtLQcdfaNOdpOj&index=7&t=307s&ab_channel=PrettyPrinted

# Working principle

It's based on Google Spreadsheet, I add all transactions through the official Google app "on the go" either with my smartphone or with my PC, and when I run the program it rearranges every transaction month-by-month to have a clean overview of my expenses.

# Needed packages
*gspread*
This package is needed to let python interact with Google Spreadsheets. To install it follow instructions on this website: https://gspread.readthedocs.io/en/latest/
*oauth2client*
This package is needed for the authentication necessary to access my personal Google Spreadsheet. Instructions here: https://pypi.org/project/oauth2client/#files
