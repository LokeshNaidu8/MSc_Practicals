# 1: data collection modelling and Compilation
import pandas
import numpy
from xlsxwriter import Workbook
mydict = {"name": ["a", "b", "c", "d", "e", "f", "g"],
          "age": [20, 22, 21, 19, 24, 18, 17],
          "designation": ["VP", "CEO", "CFO", "VP", "VP", "CEO", "CFO"]}

pf = pandas.DataFrame(mydict)
# print(pf)

'''Converts to CSV file'''
pf.to_csv('csv_fds')
df_csv = pandas.read_csv('csv_fds')
print(df_csv)

'''If you don't want duplicate index'''
pf.to_csv('csv_fds', index=False)
df_scv2 = pandas.read_csv('csv_fds')
print(df_scv2)
print('\n\n-----------------------------------\n')
'''Creating whole new table '''
names = ['lokesh', 'thinesh', 'stephen', 'divya']
grades = [76, 80, 60, 90]
bsdegreees=[1,0,0,1]
msdegrees=[3,4,3,3]
phddegrees=[0,0,1,2]
Degrees=zip(names,grades,bsdegreees,msdegrees,phddegrees)
columns=['Names','Grades','Bachelors','Masters','PHD']
data=pandas.DataFrame(data=Degrees,columns=columns)
writer=pandas.ExcelWriter('Dataframe.xlsx',engine='xlsxwriter')
data.to_excel(writer,sheet_name='Sheet1')
writer.save()
