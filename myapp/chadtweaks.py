#!/usr/bin/env python3

from flask import Flask, render_template, request, jsonify
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home1.html')


@app.route('/enternew')
def new_animal():
    return render_template('animal.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        data = request.json
        if data:
            print(data)
            nm = data["nm"]
            habitat = data["habitat"]
            group = data["group"]
        else:
            nm = request.form['nm']
            habitat = request.form['habitat']
            group = request.form['group']
        try:
            with sql.connect("database1.db") as con:
                cur = con.cursor()
                print(nm, habitat, group)
                cur.execute("INSERT INTO animals (name,habitat,group) VALUES (?,?,?)", (nm, habitat, group))
                con.commit()
                msg = "Record successfully added"
        except sql.OperationalError as err:
            try:
                con.rollback()
            except Exception:
                pass
            msg = f"error in insert operation: {err}"
        finally:
            con.close()
            return render_template("result1.html", msg=msg)


def get_animals():
    con = sql.connect("database1.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from animals")

    rows = cur.fetchall()
    return rows


@app.route('/list')
def list_animals():
    rows = get_animals()
    return render_template("list1.html", rows=rows)


@app.route('/animals')
def json_animals():
    rows = get_animals()
    data = []
    for row in rows:
        row_data = {}
        print(row)
        row_data["name"] = row["name"]
        row_data["habitat"] = row["habitat"]
        row_data["group"] = row["group"]
        data.append(row_data)
    return jsonify(data)


if __name__ == '__main__':
        conn = sql.connect('database1.db')
        print("Opened database successfully")

        conn.execute('CREATE TABLE IF NOT EXISTS animals (name TEXT, habitat TEXT, latin TEXT);')
        print("Table created successfully")
        conn.close()
        app.run(host="0.0.0.0", port=2224, debug = True)
