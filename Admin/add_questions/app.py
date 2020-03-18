from flask import Flask, url_for, render_template, redirect, request
from pymongo import MongoClient as mongoDB
import os

app = Flask(__name__)

# client = mongoDB('http://localhost:27017/') //When running locally

# client = mongoDB(os.environ['host-0f-mongo'], 27017)

db = client.questions
table = db.qcol

@app.route('/')
@app.route('/list')
def show_data():
    return render_template('index.html', name = name, table = table.find())

@app.route("/action1", methods=['POST'])
def action1():
    table.insert_one({ "name" : request.values.get("name"), "email" : request.values.get("email"), "date" : request.values.get("date"), "pr" : request.values.get("pr")})
    return redirect("/list")

@app.route("/action2", methods=['POST'])
def action2():
    old_data = {"email": request.values.get("email")}
    new_data = { "name" : request.values.get("name"), "email" : request.values.get("email"), "date" : request.values.get("date"), "pr" : request.values.get("pr")}
    table.update_one(old_data,{"$set": new_data})
    return redirect("/list")

@app.route("/action3", methods=['POST'])
def action3():
        table.delete_one({"email" : request.values.get("email")})
        return redirect("/list")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)