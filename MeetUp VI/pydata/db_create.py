import cx_Oracle

con=cx_Oracle.connect("pydatabase","contra")

cur=con.cursor()
cur.execute('create table usuarios (nombre varchar(11) not null,apellido varchar(11) not null ,dni int not null primary key, edad int not null) ')

cur.close()
con.close()