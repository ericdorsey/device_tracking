import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

# Debugging
app.debug = True


@app.route('/all_devices')
def show_all_devices():
    conn = psycopg2.connect("dbname='devices' host='localhost'")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM device;')
    result = cursor.fetchall()
    return render_template('all_devices.html', result=result)


if __name__ == '__main__':
    app.run()