#importamos la librería de Python Oracle
import oracledb

#tenemos un objeto connection(user, password, server)

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("Conectados!!!")
