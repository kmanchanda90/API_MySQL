"""Program to fetch a record via API"""
from flask import Flask, request, jsonify
import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="**********")
cursor = mydb.cursor()
app = Flask(__name__)


@app.route('/fetrec', methods=['GET', 'POST'])
def fetch_record():
    if request.method == 'POST':
        emp_id = request.json['id']
        emp_name = request.json['name']
        emp_mail_id = request.json['mail']
        emp_sal = request.json['sal']
        emp_attendance = request.json['attndnc']
        temp_var_data = f'select * from ineuron20.employee where emp_id = {emp_id} or emp_name = "{emp_name}" or emp_mail_id = "{emp_mail_id}" or emp_sal = {emp_sal} or emp_attendance = {emp_attendance}'
        cursor.execute(temp_var_data)
        return cursor.fetchall()


if __name__ == '__main__':
    app.run()
