"""Program to insert a record in MySQL table via API"""
from flask import Flask, request, jsonify
import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="**********")
cursor = mydb.cursor()
app = Flask(__name__)


@app.route('/insrec', methods=['GET', 'POST'])
def insert_record():
    if request.method == 'POST':
        emp_id = request.json['id']
        emp_name = request.json['name']
        emp_mail_id = request.json['mail']
        emp_sal = request.json['sal']
        emp_attendance = request.json['attndnc']
        temp_var_data = f'insert into ineuron20.employee values({emp_id}, "{emp_name}", "{emp_mail_id}", {emp_sal}, "{emp_attendance}")'
        cursor.execute(temp_var_data)
        mydb.commit()
        cursor.execute("select * from ineuron20.employee")
        return cursor.fetchall()


if __name__ == '__main__':
    app.run()
