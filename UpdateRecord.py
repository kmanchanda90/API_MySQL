"""Program to update a record via API"""
from flask import Flask, request, jsonify
import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="JJ62%3Q4Hd")
cursor = mydb.cursor()
app = Flask(__name__)


@app.route('/updrec', methods=['GET', 'POST'])
def update_record():
    if request.method == 'POST':
        emp_id = request.json['id']
        emp_sal = request.json['sal']
        emp_attendance = request.json['attndnc']
        temp_var_data = f'update ineuron20.employee set emp_id = {emp_id}, emp_sal = {emp_sal}, emp_attendance = {emp_attendance} where emp_name = "himmi"'
        cursor.execute(temp_var_data)
        mydb.commit()
        cursor.execute("""select * from ineuron20.employee where emp_name = 'himmi'""")
        return cursor.fetchall()


if __name__ == '__main__':
    app.run()
