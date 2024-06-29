from flask import Flask,render_template,redirect, request,url_for,send_file
from PIL import Image, ImageDraw, ImageFont
import mysql.connector

app=Flask(__name__)


def get_mysql_connection():
    return mysql.connector.connect(
        host='localhost',
        user='prathambathla',
        password='0101',
        database='blood'
    )


def generate_certificate(name, course, date, template_path='template.png', output_path='C:/Users/acerp/OneDrive/Desktop/certificate.png'):
    # Open the template image
    template = Image.open("")
    draw = ImageDraw.Draw(template)
    
    # Load a font
    font = ImageFont.truetype("arial.ttf", 20)  # Adjust the font and size as needed

    # Define text positions
    name_position = (210, 145)
    course_position = (195, 210)
    date_position = (80, 250)

    # Draw the text onto the image
    draw.text(name_position, name, font=font, fill="black")
    draw.text(course_position, course, font=font, fill="black")
    draw.text(date_position, date, font=font, fill="black")

    # Save the certificate
    template.save(output_path)




@app.route('/')
def index():
    return render_template('index.html')



@app.route('/register')
def signup():
    return render_template('register.html')


@app.route("/register",methods=["POST","GET"])
def signup1():
    
    
    username= request.form['name']
    email = request.form['email']
    college_mail=request.form['college_mail']
    phone = request.form['phone']
    age = request.form['age']
    college_name = request.form['college_name']
    dob = request.form['dob']
    address = request.form['address']
    password = request.form['password']
    role="user"
    connection = get_mysql_connection()
    cursor = connection.cursor()

    # Check if the username is already taken
    cursor.execute('SELECT * FROM all_users WHERE number = %s', (phone,))
    existing_user = cursor.fetchone()

    if existing_user:
        # Phone already exists, handle accordingly (e.g., display an error message)
        return "Phone number already exists. Please choose a different phone number."

    # If the username is unique, insert the new user into the database
    cursor.execute('INSERT INTO blood.all_users (username,email,college_mail,number,age,college_name,dob,address,password,role) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s,%s)', (username,email,college_mail,phone,age,college_name,dob,address,password,role))
    connection.commit()

    cursor.close()
    connection.close()

    # Successful signup, you can redirect to a login page or another page
    return "Account created successfully"


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST','GET'])
def login1():

    phone = request.form['phone']
    password = request.form['password']
    role=request.form['role']

    connection = get_mysql_connection()
    cursor = connection.cursor(dictionary=True)
    #if role=="user":
    cursor.execute('SELECT * FROM blood.all_users WHERE number = %s AND role = %s AND password = %s', (phone,role, password))
    user = cursor.fetchone()
    cursor.execute('SELECT QUANTITY FROM blood.all_users WHERE number = %s AND role = %s AND password = %s', (phone,role, password))
    quantity = cursor.fetchone()

    cursor.close()
    connection.close()
    if user:
        # Successful login, you can redirect to a dashboard or another page

        return render_template("user-dashboard.html",saved_lives=quantity)
        
    else:
        # Invalid credentials, redirect back to the login page
          return "phone or password is incorrect"
        


@app.route("/find-blood")
def findblood():
    return render_template("findblood.html")

@app.route("/aboutus")
def aboutus():
    return send_file("static/cons.jpg", mimetype='image/jpg')

@app.route('/events')
def events():
    return send_file("static/cons.jpg", mimetype='image/jpg')
@app.route("/update-user-donations")
def update_user_donations():
    username = request.form['username']
    act = request.form['action']
    quantity = request.form['quantity']

    connection = get_mysql_connection()
    cursor = connection.cursor(dictionary=True)

    if act == "donated":
        cursor.execute('SELECT donated_quantity FROM users WHERE username = %s', (username))
        donated_quantity = cursor.fetchone()['donated_quantity']
        donated_quantity = int(donated_quantity) + int(quantity)
        cursor.execute('UPDATE users SET donated_quantity = %s WHERE username = %s', (donated_quantity,username))
        connection.commit()

        generate_certificate(username, "Blood Donation", "June 28, 2024")
        

    else:
        cursor.execute('SELECT donated_quantity FROM users WHERE username = %s', (username))
        donated_quantity = cursor.fetchone()['donated_quantity']
        donated_quantity = int(donated_quantity) - int(quantity)
        cursor.execute('UPDATE users SET donated_quantity = %s WHERE username = %s', (donated_quantity,username))
        connection.commit()

    cursor.close()
    connection.close()
    
    return "updation successful"

@app.route('/find')
def find():
    return render_template("findblood.html")



@app.route('/donor')
def donor():
    return render_template("donor.html")


@app.route('/acceptor')
def acceptor():
    return render_template("acceptor.html")



@app.route('/community')
def community():
    return render_template("community.html")

@app.route('/rewards')
def rewards():
    return render_template("Rewards.html")
@app.route('/logout')
def logout():
    return render_template("logout.html")

@app.route('/demonstration')
def demonstration():
    return render_template("demonstration.html")


@app.route('/register-mod')
def register_mod():
    return render_template("register-mod.html")
    
@app.route('/register-admin')
def register_admin():
    return render_template("register-admin.html")

app.run(debug=True)