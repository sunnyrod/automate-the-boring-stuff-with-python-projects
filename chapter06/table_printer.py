tableData = [['apples', 'oranges', 'cherries', 'banana'],
	     ['Alice', 'Bob', 'Carol', 'David'],
	     ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
	# find longest word per column
	colWidths = [0] * len(table)
	for col in range(len(table)):
		for elem in table[col]:
			colWidths[col] = max(colWidths[col], len(elem))

	# print each column with right-justification
	cols = len(table)
	rows = len(table[0])
	for row in range(rows):
		for col in range(cols):
			print(table[col][row].rjust(colWidths[col]), end=' ')
		print()

printTable(tableData)