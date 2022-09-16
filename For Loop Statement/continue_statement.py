"""
The continue Statement
Do not print mango
"""

fruits = ['Orange','Banana','Mango','Melon','Pear']
for x in fruits:
    if x == 'Mango':
        continue
    print(x)