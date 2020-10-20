import rdm6300
import MySQLdb

# Establish connection to MYSQL Server

dbConn = MySQLdb.connect("localhost","root","","raspberry_testing") or die ("Could not connect to the databases")

# Open the database

cursor = dbConn.cursor()

try:
	print("Trying..."),device
	device = rdm6300.Reader('/dev/ttyUSB0')
except:
	print("Failed to connect on"),device
while True:
	try:
		card = reader.read()
		print (card)
		try:
			cursor=dbConn.cursor()
			cursor.execute("""INSERT INTO `Test1` (ID) VALUES (NULL)""")
			dbConn.commit()
			dbConn.close()
		except MySQLdb.IntegrityError:
			print ("Failed to insert data")
		finally:
			cursor.close()
	except:
		print ("Processing")



