import cx_Oracle
import csv

con=cx_Oracle.connect("pydatabase","contra")
cur=con.cursor()
 
with open('names.csv') as File:
	reader = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
	for row in reader :
		order="INSERT INTO usuarios VALUES ("
		order+="'"+row[0]+"',"
		order+="'"+row[1]+"',"
		order+= row[2]+","
		order+= row[3]+")"
		#print(order)
		cur.execute(order)
cur.execute('commit')
cur.close()
con.close()