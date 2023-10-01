import csv

def doTheCounting(input):
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
        input.apppend(row)
    output = doTheCounting(input)

print(output)