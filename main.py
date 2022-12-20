import mysql.connector
from flask import Flask, url_for, request, render_template, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", ueberschrift="Willkommen")


@app.route("/einfuegen")
def einfuegen():
    return render_template("insert1.html", titel="In Datenbank einfügen")


@app.route("/eingefuegt", methods=["POST"])
def eingefuegt():
    vorname = request.form["vorname"]
    nachname = request.form["nachname"]
    telefonnr = request.form["telefonnr"]
    strasse = request.form["strasse"]
    hausnr = request.form["hausnr"]
    wohnort = request.form["wohnort"]

    sql = "INSERT INTO personen (vorname, nachname, telefonnr, strasse, hausnr, wohnort, profile) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (vorname, nachname, telefonnr, strasse, hausnr, wohnort, "Profilbilder/")

    mycursor.execute(sql, val)
    mydb.commit()

    return render_template("insert2.html", vorname=vorname, nachname=nachname)


@app.route("/show", methods=["GET"])
def show():
    sql = "SELECT id, vorname, nachname, telefonnr, strasse, hausnr, wohnort FROM personen"
    mycursor.execute(sql)
    data = mycursor.fetchall()

    return render_template("show.html", sql=sql, data=data)


if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host="192.168.0.69",
        user="john",
        password="phpmyadminapache",
        database="adressverwaltung"
    )
    mycursor = mydb.cursor(buffered=True)
    app.run(port=1337, debug=True)
