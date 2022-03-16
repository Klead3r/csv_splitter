import csv
import sys

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

fileName = input("Filename:")
rowsPerFile = input("Rows per output file:")

newFiles = []
rowCounter = -1
fileCounter = 0
headerRow = []

sys.stdout.write('\nSplitting file rows...\n')

with open(fileName, encoding='utf-8', errors='ignore') as file:
    rows = csv.reader(file)
    for row in rows:
        if (rowCounter == -1 and fileCounter == 0):
            headerRow = row
            newFiles.append([])
            newFiles[fileCounter].append(headerRow)
            rowCounter = 0
        else:
            if (rowCounter >= int(rowsPerFile)):
                rowCounter = 0
                fileCounter = fileCounter + 1
                newFiles.append([])
                newFiles[fileCounter].append(headerRow)

            newFiles[fileCounter].append(row)
            rowCounter = rowCounter + 1

sys.stdout.write('\nWriting new files...\n')

for file in range(0, len(newFiles)):
    splitFileName = fileName + '_' + str(file) + '.csv'
    with open(splitFileName, 'w+') as f:
        writer = csv.writer(f)
        writer.writerows(newFiles[file])

sys.stdout.write('\nDone!\n')