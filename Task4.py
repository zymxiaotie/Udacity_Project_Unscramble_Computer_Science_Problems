"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
import time

def task4(calls, texts):
    start_time = time.time()
    telemarketers = set()
    outgoing_calls = set(call[0] for call in calls)
    incoming_calls = set(call[1] for call in calls)
    send_texts = set(text[0] for text in texts)
    receive_texts = set(text[1] for text in texts)

    for call in outgoing_calls:
        if call not in incoming_calls and call not in send_texts and call not in receive_texts:
            telemarketers.add(call)

    for number in sorted(telemarketers):
        print(number)

    end_time = time.time()
    print(f"Wall time:{end_time-start_time} seconds")


    
task4(calls, texts)



