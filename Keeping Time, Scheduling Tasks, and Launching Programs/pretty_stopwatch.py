# python3
# pretty_stopwatch.py
# prints a simple stopwatch to terminal, and optionally copies the stopwatch output to the user's clipboard

import time
import pyperclip

def main():
    copy_string = begin_stopwatch()
    end_stopwatch(copy_string)

def begin_stopwatch():
    print('\nPress enter to begin your stopwatch. Press enter again to mark a new lap. Press Ctrl-C to stop the stop-watch.', end='')
    input()

    start_time = time.time()
    last_time = start_time
    lap = 1
    full_string = ''
    while True:
        try:
            input()
            
            now = time.time()
            lap_str = str(lap).rjust(2)
            total_time_str = str(round(now - start_time, 2)).rjust(7)
            lap_time_str = str(round(now - last_time, 2)).rjust(6)
            
            lap_string = f'Lap #{lap_str}:{total_time_str} ({lap_time_str})'
            print(lap_string, end='')
            full_string += lap_string +'\n'
            
            last_time = now
            lap += 1
            
        except KeyboardInterrupt:
            return full_string

def end_stopwatch(copy_string):
    print('\n\nCopying output to clipboard. Press Ctrl-C to cancel.\n')
    try:
        time.sleep(3)
        pyperclip.copy(copy_string)
        print('Output copied')
    except KeyboardInterrupt:
        print ('Output NOT copied.')
    print('Done.')

if __name__ == '__main__':
    main()