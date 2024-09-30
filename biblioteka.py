"""
from termcolor2 import c

print(c ('Some text').blue.on_white.underline)
print('Datorika')
print(c('Jauna rindkopa').red)
print()

from termcolor import colored
text = colored('Hello, word!', 'red', attrs=['bord'])
print(text)


#no wkipedia
import wikipedia
wikipedia.set_lang('lv')
print(wikipedia.summary('Riga'))
print()

#Таблица 
from prettytable import PrettyTable
table=PrettyTable()
table.field_names= ['Name', 'Age', 'City']
table.add_row (['Tom', '15', 'Riga'])
print(table)
"""

#Графики
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('Funkcijas grafiks')
plt.show()