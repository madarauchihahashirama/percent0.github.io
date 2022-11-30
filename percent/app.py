import sqlite3
from flask import Flask ,render_template,request
app=Flask (__name__)
db=sqlite3.connect("manu.db;",check_same_thread=False)
co=db.cursor()
@app.route("/")
def main():
	return render_template("L1.html")

@app.route("/la",methods=["post"])
def per():
	yname=request.form.get("f")
	lname=request.form.get("fc")
	if yname=="might" and lname=="guy":
		loer=co.execute("SELECT * from names")
		return render_template("secret.html",loer=loer)
	else:
		
		n=len(yname)
		m=len(lname)
		per=((m+n)*5*92)/100
		co.execute("INSERT into names(name1,name2) values(?,?)",(yname,lname))
		db.commit()
		return render_template("show.html",per=per)


if __name__=="__main__":
	app.run(debug=True)
	