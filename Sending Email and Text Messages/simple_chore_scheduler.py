import openpyxl
import ezgmail
import shelve

# copy excel input validation function

# workbook dict { workbook : most recent chore assignment } allows storing data for multiple different workbooks
# chore assignment dict { email address : string of chores} records the most recent chore assignment by address

# create a random chore grouping
# create list of chore assignment dicts by cycling through addresses
# remove the most recent chore assignment dict from this list
# select a random dict
# email accordingly
# update chore assignment dict (stored in shelve data file)