tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    print('\n')
    for i, item in enumerate(table[0]):
        for row in table:
            print(row[i].rjust(max(map(lambda x: len(x), row)))),
        print('\n')
            
printTable(tableData)
