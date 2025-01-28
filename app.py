from flask import Flask,render_template,redirect, request,url_for,send_file,session, jsonify
from PIL import Image, ImageDraw, ImageFont
from flask_mail import Mail,Message
import mysql.connector
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

app=Flask(__name__)
app.secret_key = '0123'


def get_mysql_connection():
    return mysql.connector.connect(
        host='localhost',
        user='anirudh',
        password='0101',
        database='blood'
    )

# Email configuration 
mail_config = {
    "MAIL_SERVER": "smtp.gmail.com",
    "MAIL_PORT": 465 ,
    "MAIL_USE_TLS": False,  
    "MAIL_USE_SSL":True,
    "MAIL_USERNAME": "",
    "MAIL_PASSWORD": "",
    "MAIL_DEFAULT_SENDER" :""
}

app.config.update(mail_config)
mail = Mail(app)


# Sample data for donors and blood banks
data = {
    'donor_blood_type': ['A+', 'O-', 'B+', 'A+', 'AB+', 'O-', 'B+', 'A-', 'O-', 'AB+', 'B+'],
    'blood_bank_needed_blood_type': ['A+', 'O-', 'B+', 'A-', 'AB+', 'O-', 'B+', 'A+', 'O-', 'AB+', 'A+'],
    'proximity_km': [5, 10, 15, 12, 7, 8, 9, 13, 6, 7, 14],
    'last_donation_days_ago': [45, 90, 30, 50, 60, 120, 40, 75, 95, 85, 25],
    'blood_bank_urgency': [3, 5, 4, 2, 4, 5, 3, 1, 4, 3, 5],  # 1 (Low) to 5 (High)
    'successful_match': [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0]  # 1: successful, 0: unsuccessful
}

# Convert the data into a Pandas DataFrame
df = pd.DataFrame(data)

# Map blood types to numerical values
blood_type_mapping = {'O-': 0, 'O+': 1, 'A-': 2, 'A+': 3, 'B-': 4, 'B+': 5, 'AB-': 6, 'AB+': 7}
df['donor_blood_type'] = df['donor_blood_type'].map(blood_type_mapping)
df['blood_bank_needed_blood_type'] = df['blood_bank_needed_blood_type'].map(blood_type_mapping)

# Features (X) and target (y)
X = df[['donor_blood_type', 'blood_bank_needed_blood_type', 'proximity_km', 'last_donation_days_ago', 'blood_bank_urgency']]
y = df['successful_match']

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)




def cfgenerator(name,units,date):
    template = Image.open("./static/template.jpg")
    draw = ImageDraw.Draw(template)
    
    # Load a font
    font = ImageFont.truetype("arial.ttf", 20)  # Adjust the font and size as needed

    # Define text positions
    name_position = (750, 450)
    txt_pos=(600,620)
    don_unit = (875, 620)
    date_position = (900, 700)

    # Draw the text onto the image
    draw.text(name_position, name, font=font, fill="red")
    draw.text(txt_pos, "that he donated blood units =", font=font, fill="black")
    draw.text(don_unit, units, font=font, fill="black")
    draw.text(date_position, date, font=font, fill="black")

    # Save the certificates    
    save_path= "./certificates/"+str(name)+".jpg"
    template.save(save_path)



@app.route('/')
def index():
    if 'username' in session:
        # User is logged in, pass the username to the template
        username = session['username']
        quantity=session['quantity']

        return render_template("user-dashboard.html", username=username,quantity=quantity)
    else:
        # User is not logged in, redirect to login page
        return redirect(url_for('login'))
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = get_mysql_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute('SELECT * FROM blood.donors WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()

        cursor.execute('SELECT quantity FROM blood.donors WHERE username = %s', (username,))
        quantity= cursor.fetchone()

        cursor.close()
        connection.close()

        if user:
            # Store username in session
            session['username'] = username
            session['quantity'] = quantity
            return redirect(url_for('index'))
        else:
            return "Username or password is incorrect"
    
    return render_template('login.html')


@app.route("/register",methods=["POST","GET"])
def signup1():
    if request.method == 'POST':
    
        username= request.form['name']
        email = request.form['email']
        college_mail=request.form['college_mail']
        phone = request.form['phone']
        age = request.form['age']
        college_name = request.form['college_name']
        dob = request.form['dob']
        address = request.form['address']
        password = request.form['password']
        blood_group= request.form['blood_group']
        role="donor"
        connection = get_mysql_connection()
        cursor = connection.cursor()
        

        # Check if the username is already taken
        cursor.execute('SELECT * FROM donors WHERE username = %s', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            # Phone already exists, handle accordingly (e.g., display an error message)
            return "Phone number already exists. Please choose a different phone number."

        # If the username is unique, insert the new user into the database
        cursor.execute('INSERT INTO blood.donors (username,email,college_mail,numb,age,college_name,dob,address,password,role,blood_group) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s,%s,%s)', (username,email,college_mail,phone,age,college_name,dob,address,password,role,blood_group))
        connection.commit()

        cursor.close()
        connection.close()

        # Successful signup, you can redirect to a login page or another page
        return redirect(url_for('login'))
    

    return render_template('register.html')


@app.route('/logout')
def logout():
    # Remove user from session
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/bblogin', methods=['GET', 'POST'])
def bblogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = get_mysql_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute('SELECT * FROM bb WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:
            # Store username in session
            session['username'] = username
            return redirect(url_for('bloodbank'))
        else:
            return "Username or password is incorrect"
    
    return render_template('bblogin.html')

@app.route("/bloodbank", methods=["GET", "POST"])
def bloodbank():
    if request.method == 'POST':
        username = request.form['username']
        units = int(request.form['units'])  # Convert units to integer
        blood_group = request.form['blood_group']
        action = request.form['action']
        date=request.form['date']


        # Ensure action is valid
        if action not in ("D", "A"):
            return "Invalid Action"
        
        connection = get_mysql_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            if action == "D":  # Donation, add units
                cfgenerator(username,str(units),date)
                cursor.execute(
                    'UPDATE donors SET QUANTITY = QUANTITY + %s WHERE BLOOD_GROUP = %s AND username = %s',
                    (int(units), blood_group, username)
                )


            else:  # Action is "A" (Accepted), subtract units
                # Check if the donor has enough units
                cursor.execute(
                    'SELECT quantity FROM donors WHERE blood_group = %s AND username = %s',
                    (blood_group, username)
                )
                result = cursor.fetchone()
                if result and result['quantity'] >= units:
                    cursor.execute(
                        'UPDATE donors SET quantity = quantity - %s WHERE blood_group = %s AND username = %s',
                        (units, blood_group, username)
                    )
                else:
                    # Handle insufficient units
                    return "Insufficient units for the donor"

            connection.commit()
        except Exception as e:
            # Handle exceptions gracefully
            return f"An error occurred: {e}"
        finally:
            cursor.close()
            connection.close()

        return render_template('bloodbank.html')
    else:
        return render_template('bloodbank.html')


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

        # generate_certificate(username, "Blood Donation", "June 28, 2024")
        

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