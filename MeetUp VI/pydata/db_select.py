import cx_Oracle
import matplotlib.pyplot as plt
import numpy as np

con=cx_Oracle.connect("pydatabase","contra")

cur=con.cursor()
cur.execute('select edad from usuarios')
res=0
lis=[]
for result in cur:
	print(result)
	lis+=[result[0]]

print(lis)
plt.plot(lis)
plt.show()

cur.close()
con.close()