import psycopg2
from flask import Flask,render_template, request
from flask import redirect, url_for
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
@app.route('/register')
def register():
    return render_template('Reg.html')
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    cursor = conn.cursor()
    cursor.execute("INSERT INTO log_in (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    conn.commit()
        return.redirect(url_for('courses.html'))
                
@app.route('/courses')
def courses():
    return render_template("courses.html")

@app.route('/about')
def about():
    return render_template("about_us.html")

@app.route('/alumni')
def alumni():
    return render_template("alumni.html")
if __name__ == '__main__':
    app.run(debug=True)
    
