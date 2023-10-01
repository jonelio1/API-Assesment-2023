import csv
import json

def doTheCounting(input): ##It does the counting.
    output = {}
    for unit in input:
        if unit in output.keys():
            output[f'{unit}'] = output[f'{unit}'] + 1
        else:
             output[f'{unit}'] = 1
    return output

input = []
with open('input.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        input += row
    output = doTheCounting(input)

print(output)
with open('output.json', 'w') as f:
    json.dump(output, f)