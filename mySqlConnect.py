''' mysql test '''
import mysql.connector
from mysql.connector import errorcode

try:
    
    config = {
          'user': 'testUser',
          'password': 'test',
          'host': 'localhost',
          'database': 'macroeconomics_series',
          'raise_on_warnings': True,
          }
  
    cnx = mysql.connector.Connect(**config)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
    
# request

# close the connection    
cnx.close()
  
