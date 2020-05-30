from flask import *
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
	global rows1
	global rows2
	global stat0
	global column
	column=[]
	stat0=""
	con = sqlite3.connect("DashboardProject.db")
	con.row_factory = sqlite3.Row
	cur = con.cursor()
	cur.execute("select Distinct circle from ProjectTable")
	rows1 = cur.fetchall()
	cur.execute("select *  from ProjectTable")
	rows2 = cur.fetchall()
	colnames = cur.description
	for Allcolumns in colnames:
		column.append(Allcolumns[0])
	return render_template("view.html",rows1=rows1,rows2=rows2,column=column)

@app.route("/viewTable", methods=["GET"])
def viewTable():
	global stat
	print("test1")
	status =request.args.get('Status')
	print("Status",status)
	stat=status
	return render_template("view.html",stat=stat,rows1=rows1,stat0=stat0,rows2=rows2,column=column)

@app.route("/viewTable1", methods=["GET"])
def viewTable1():
	print("test1")
	status0 =request.args.get('Status1')
	print("Status",status0)
	stat0=status0
	con = sqlite3.connect("DashboardProject.db")
	con.row_factory = sqlite3.Row
	cur = con.cursor()
	cur.execute("select *  from ProjectTable where circle = '{0}'".format(stat0))
	rows2 = cur.fetchall()
	return render_template("view.html",stat0=stat0,rows1=rows1,stat=stat,rows2=rows2,column=column)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9092)
