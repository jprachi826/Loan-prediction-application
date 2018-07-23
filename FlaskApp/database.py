from flask import Flask 
from flask_mysqldb import MySQL 

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ci'
mysql = MySQL(app)

@app.route('/')
def index():
	cur = mysql.connection.cursor()
	cur.execute('''SELECT Name FROM user WHERE Id = 5''')
	rv = cur.fetchall()
	return str(rv)

@app.route('/addone')
def addone():
	cur = mysql.connection.cursor()
	#cur.execute('''SELECT MAX(id) FROM example''')
	#maxid = cur.fetchone() #(10,)
	cur.execute('''INSERT INTO user (Name,DOB,Email,Password,first_login) VALUES (%s, %s,, %s, %s, %s)''', ('abc','16/11/1997','crc@gmaul.com','123',0))
	mysql.connection.commit()
	return "Done"


if __name__ == '__main__':
	app.run(debug=True)