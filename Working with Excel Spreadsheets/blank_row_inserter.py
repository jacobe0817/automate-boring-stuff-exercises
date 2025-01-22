import sys
import os
import openpyxl

try:
    insert_index = int(sys.argv[1])
    insert_width = int(sys.argv[2])
    file_path = ' '.join(sys.argv[3:])
except:
    print('\nCommand line arguments must be 2 integers (start index of gap and width of gap) followed by the spreadsheet path\nSpaces are allowed in the path\n.xlsx extension is optional')
    sys.exit()

if not file_path.endswith('.xlsx'):
    file_path += '.xlsx'

file_path = os.path.abspath(file_path)

if not os.path.exists(file_path):
    print(f'\nFile {file_path} not found')
    sys.exit()

print(f'\nOpening file at {file_path}')
workbook = openpyxl.load_workbook(file_path)
sheet = workbook.active

new_file_name = 'updated ' + os.path.basename(file_path)
new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

print('\nInserting rows')
sheet.insert_rows(insert_index, insert_width)

print(f'\nSaving updated file to {new_file_path}')
workbook.save(new_file_path)

print('\nDone.')