
# from flask import Flask, render_template,request
# from flask_mysqldb import MySQL
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os
import subprocess

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'finalyearprojectdb'

mysql = MySQL(app)
app.secret_key = 'your secret key'

@app.route("/")
def main():
    return render_template('home.html')

@app.route('/login' , methods=['GET', 'POST'])       
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = % s AND password = % s', (username, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['username'] = account['username']
            session['password'] = account['password']
            print('Logged in successfully !')
            return render_template('home.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)


@app.route("/signup",methods=['GET','POST'])
def transaction():
    if request.method == 'POST':
        un = request.form.get('username')
        email = request.form.get('email')
        pasw = request.form.get('password')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user (username ,  email , password) VALUES (%s,%s,%s)" , (un,email,pasw))
        mysql.connection.commit()
        cur.close()
        print("success")
        return render_template('home.html' )
    else:
        print("did not insert")
    return render_template('register.html' )

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/lstm-intro")
def lstm():
    return render_template("lstm.html")

@app.route("/yolo-main")
def yolo():
    return render_template('yolo.html')

@app.route("/lstm1")
def lstm1():
    return render_template('lstm1.html')

@app.route("/lstm2")
def lstm2():
    return render_template('lstm2.html')


@app.route("/lstm3")
def lstm3():
    return render_template('lstm3.html')


@app.route("/lstm4")
def lstm4():
    return render_template('lstm4.html')


@app.route("/lstm5")
def lstm5():
    return render_template('lstm5.html')


@app.route("/lstm6")
def lstm6():
    return render_template('lstm6.html')

#cam functions
#yolo
@app.route('/yolo-words-detect')
def opencam1():
    print("route accesed")

    subprocess.run(['python','detect_yolo_words.py', '--source', '0'],shell=True)
    # subprocess.run(['python', 'detect.py','--source', '0'],shell=True)
    return render_template("yolo.html")

@app.route('/yolo-alpha-detect')
def opencam2():
    print("route accesed")
    subprocess.run(['python','detect_yolo_alpha.py', '--source', '0'],shell=True)
    # subprocess.run(['python', 'detect.py'],shell=True)
    return render_template("yolo.html")

#lstm
@app.route('/lstm-detect-1')
def opencam3():
    print("route accesed")

    # subprocess.run(['python','detect_yolo_words.py', '--source', '0'],shell=True)
    subprocess.run(['python', 'detect.py'],shell=True)
    return "success"  

@app.route('/lstm-detect-2')
def opencam4():
    print("route accesed")

    # subprocess.run(['python','detect_yolo_words.py', '--source', '0'],shell=True)
    subprocess.run(['python', 'detect.py'],shell=True)
    return "success"        

@app.route('/lstm-detect-3')
def opencam5():
    print("route accesed")

    # subprocess.run(['python','detect_yolo_words.py', '--source', '0'],shell=True)
    subprocess.run(['python', 'detect.py'],shell=True)
    return "success"        

@app.route('/lstm-detect-4')
def opencam6():
    print("route accesed")

    # subprocess.run(['python','detect_yolo_words.py', '--source', '0'],shell=True)
    subprocess.run(['python', 'detect.py'],shell=True)
    return "success"        

@app.route('/lstm-detect-5')
def opencam7():
    print("route accesed")

    # subprocess.run(['python','detect_yolo_words.py', '--source', '0'],shell=True)
    subprocess.run(['python', 'detect.py'],shell=True)
    return "success"        
      
@app.route('/lstm-detect-6')
def opencam8():
    print("route accesed")

    # subprocess.run(['python','detect_yolo_words.py', '--source', '0'],shell=True)
    subprocess.run(['python', 'detect.py'],shell=True)
    return "success"        

    
if __name__ == "__main__":
    app.debug = True
    app.run()