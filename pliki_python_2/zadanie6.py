tableData = [['jabłka','pomarańcze','wiśnie','banany'],
              ['Alicja','Bob','Karol','Dawid'],
              ['psy','koty','łosie','gęsi']]

def printTable(tData):
    colWidth = [0] * len(tData)
    for col in range(len(tData)):
        for row in range(len(tData[0])):
            entryLength = len(tData[col][row])
            if(entryLength > colWidth[col]):
                colWidth[col] = entryLength
    for row in range(len(tData[0])):
        for col in range(len(tData)):
            print(tData[col][row].rjust(colWidth[col]) + ' ', end='')
        print()

printTable(tableData)

