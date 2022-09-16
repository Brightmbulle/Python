"""
The Break Statement.
Exit the loop when x is "mango":
"""

fruits = ['Orang','banana','mango','melon','pear']
for x in fruits:
    print(x)
    if x == 'mango':
        break


    #Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ['Orang','banana','mango','melon','pear']
for x in fruits:
    if x == 'mango':
        break
    print(x)