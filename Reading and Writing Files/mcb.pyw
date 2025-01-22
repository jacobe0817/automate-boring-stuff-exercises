import pyperclip
import shelve
import sys

#py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#py.exe mcb.pyw <keyword> - Loads keyword's associated text to clipboard
#py.exe mcb.pyw list - Loads all keywords to clipboard
#py.exe mcb.pyw delete <keyword> - Deletes a keyword from the shelf
#py.exe mcb.pyw delete - Deletes all keywords from the shelf
with shelve.open('mcb_keywords') as keywords_file:
    arg_1 = sys.argv[1].lower()
    if len(sys.argv) == 2:
        if arg_1 == 'list':
            pyperclip.copy(str(list(keywords_file.keys())))
        elif arg_1.lower() == 'delete':
            for key in list(keywords_file.keys()):
                del keywords_file[key]
        else:
            pyperclip.copy(keywords_file[arg_1])
    elif len(sys.argv) == 3:
        arg_2 = sys.argv[2].lower()
        if arg_1 == 'save':
            keywords_file[arg_2] = pyperclip.paste()
        elif arg_1 == 'delete':
            del keywords_file[arg_2]