"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
import time

def task2(calls):
    start_time = time.time() 
    call_time = {}
    for call in calls:
        if call[0] not in call_time:
            call_time[call[0]] = int(call[3])
        else:
            call_time[call[0]] += int(call[3])
        if call[1] not in call_time:
            call_time[call[1]] = int(call[3])
        else:
            call_time[call[1]] += int(call[3])
    longest_time = max(call_time.values())
    for number, t in call_time.items():
        if t == longest_time:
            print(f"{number} spent the longest time, {t} seconds, on the phone during September 2016.")
    
    end_time = time.time()
    print(f"Wall time:{end_time-start_time} seconds")

task2(calls)
