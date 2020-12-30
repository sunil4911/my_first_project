#!flask/bin/python
import json
import mysql.connector
from flask import Flask, Response, render_template
from helloworld.flaskrun import flaskrun

application = Flask(__name__)

connection = mysql.connector.connect(
    host="my-first-project-db.crnpdg0lmdqp.us-east-2.rds.amazonaws.com",
    user="admin",
    password="M012599g",
    database="my_first_project_db"
)

db = connection.cursor(dictionary=True)
@application.route('/', methods=['GET'])
def get():
    db.execute("select * from people")
    result = db.fetchall()
    return render_template("addresses.html", addresses=result)



if __name__ == '__main__':
    flaskrun(application)
