"""Program to delete a record via API"""
from flask import Flask, request, jsonify
import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", passwd="**********")
cursor = mydb.cursor()
app = Flask(__name__)


@app.route('/delrec', methods=['GET', 'POST'])
def delete_record():
    if request.method == 'POST':
        emp_id = request.json['id']
        temp_var_data = f'delete from ineuron20.employee where emp_id = {emp_id}'
        cursor.execute(temp_var_data)
        mydb.commit()
        cursor.execute("select * from ineuron20.employee")
        return cursor.fetchall()


if __name__ == '__main__':
    app.run()
