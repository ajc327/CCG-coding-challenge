import sqlite3 
import json 
from sqlite3 import Error
 

def read_users():
	with open("users.json", "r") as f:
		users  = json.load(f)
	return users 
 
 
def create_connection(db_file):
	""" create a database connection to a SQLite database """
	try:
		conn = sqlite3.connect(db_file)

		print(sqlite3.version)
	except Error as e:
		print(e)
	finally:
		cursor = conn.cursor()
		

		users_data = read_users()
		users_list = [list(users_data[k].values()) for k in range(len(users_data))]
			
		#print (users_list)
		try:
			cursor.execute("""CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT, password TEXT,
			title TEXT, firstname TEXT, middleInitial TEXT, lastname TEXT, institute TEXT,dateOfBirth TEXT)
			
			""")
		except:
			pass 
			
		try:
			cursor.executemany(''' INSERT INTO users(id, username, password,
			title, firstname, middleInitial, lastname, institute,dateOfBirth) VALUES(?,?,?,?,?,?,?,?,?)''', users_list)
			conn.commit()	
		except:
			pass
			
		conn.close()
		return conn
 

	
	
if __name__ == '__main__':
	create_connection("pythonsqlite.db")

	a = read_users()
	