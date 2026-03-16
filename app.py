import psycopg2
from flask import Flask,render_template, request
app = Flask(__name__)
conn=psycopg2.connect(
        host="localhost",
        database="edify",
        user="postgres",
        password="123456",
        port="5432"
    )
# Route to handle POST requests and insert data into the database
@app.route('/')
def home():
    return(render_template('index.html'))
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    conn.commit()
    return"Data inserted successfully!"
if __name__ == '__main__':
    app.run(debug=True)
    