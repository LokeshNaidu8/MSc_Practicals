import sqlite3

conn = sqlite3.connect('Datasets/portal_mammals.sqlite')
cursor = conn.cursor()
cursor.execute('select * from species')
a = cursor.fetchall()
for i in a:
    print(i)

cursor.execute("select species from species where taxa='bird'")
b=cursor.fetchall()
print(b)

cursor.execute("select plot_id from plots where plot_type='Control'")
c=cursor.fetchall()
print(c)


import pandas
cars={'Brands':['Honda','Suzuki','Bugatti','Mazda'],
      'Price':[290000,300000,40000000,120000000]}
dt=pandas.DataFrame(data=cars,columns=('Brands','Price'))

import sqlite3

conn=sqlite3.connect('TestDB1.db')
c=conn.cursor()
# c.execute('Create table Cars (Brands varchar(20),Price int)')
# conn.commit()
dt.to_sql('Cars',conn,if_exists='replace',index=False)
print('\n\n')
c.execute('select brands,price from cars where price=(select max(price) from cars)')
result=c.fetchone()
print(result)