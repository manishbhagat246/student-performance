from flask import Flask,request,render_template,make_response
import mysql.connector
import pandas as pd
from mysql.connector import Error
from werkzeug.utils import secure_filename
import os
import json
import csv
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


app = Flask(__name__)
connection = mysql.connector.connect(host='localhost',user='root',password='')
student_db='CREATE DATABASE IF NOT EXISTS student_db;'
userdata='CREATE TABLE IF NOT EXISTS userdata( id int AUTO_INCREMENT PRIMARY KEY,name varchar(50),email varchar(100),pass varchar(50),ph varchar(10),dob varchar(10),gender varchar(10) );'
dataset='CREATE TABLE IF NOT EXISTS dataset( gender varchar(10),race varchar(50),parental varchar(50),lunch varchar(50),test_prep varchar(10),math_score int,reading_score int,writing_score int );'
cursor = connection.cursor()
cursor.execute(student_db)
connection = mysql.connector.connect(host='localhost',user='root',password='',database='student_db')
cursor = connection.cursor()
cursor.execute(userdata)
cursor.execute(dataset)
fn = "./static/uploads/exams.csv"
        # initializing the titles and rows list 
fields = [] 
rows = []
  
def savedata(fn):
    connection = mysql.connector.connect(host='localhost',user='root',password='',database='student_db')
    cursor = connection.cursor()
    deletequery="delete from dataset"
    cursor.execute(deletequery)
    with open(fn, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
        try:
            for row in rows[1:]:
                # parsing each column of a row
                if row[0][0] != "":
                    # data doesn't exist, insert into the database
                    query = "INSERT INTO dataset VALUES ("
                    for col in row:
                        query += '"' + col + '",'
                    query = query[:-1] + ");"
                    # print("query: " + str(query), flush=True)
                    cursor.execute(query)
                    connection.commit()

        except Exception as e:
            print(f"An exception occurred: {str(e)}")
    connection.close()
    cursor.close()

savedata(fn)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    return render_template('register.html')

@app.route('/regdata', methods =  ['GET','POST'])
def regdata():
    #Data gathering
    nm=request.args['username']
    em=request.args['email']
    ph=request.args['phone']
    gen=request.args['gender']
    pswd=request.args['password']
    dob=request.args['dob']

    
    #Data transmission to db
    connection = mysql.connector.connect(host='localhost',database='student_db',user='root',password='')
    sqlquery="insert into userdata(name,email,ph,gender,pass,dob) values('"+nm+"','"+em+"','"+ph+"','"+gen+"','"+pswd+"','"+dob+"')"
    print(sqlquery)
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    connection.commit() 
    connection.close()
    cursor.close()
    msg="Data Saved Successfully"
    #return render_template('register.html')
    resp = make_response(json.dumps(msg))
    
    print(msg, flush=True)
    #return render_template('register.html',data=msg)
    return resp



@app.route('/logdata', methods =  ['GET','POST'])
def logdata():
    #Data gathering
    em=request.args['email']
    pswd=request.args['password']

    
    #Data transmission to db
    connection = mysql.connector.connect(host='localhost',database='student_db',user='root',password='')
    sqlquery="select count(*) from  userdata where email='"+em+"' and pass='"+pswd+"'"
    print(sqlquery)
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    data=cursor.fetchall()
    print(data) 
    connection.close()
    cursor.close()
    msg=""
    if data[0][0]==0:
        msg="Failure"
    else:
        msg="Success"
    
    print(msg, flush=True)
    #return render_template('register.html',data=msg)
    return msg
    

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    connection = mysql.connector.connect(host='localhost',database='student_db',user='root',password='')
    sqlquery="select count(*) from dataset group by gender"
    sqlqueryr="select count(*) from dataset group by race"
    sqlqueryp="select count(*) from dataset group by parental"
    sqlqueryt="select count(*) from dataset group by test_prep"
    sqlqueryl="select count(*) from dataset group by lunch"
    sqlquerymath="select math_score from dataset "
    sqlquerywrite="select writing_score from dataset  "
    sqlqueryread="select reading_score from dataset "
    mathmale="select math_score from dataset where gender='male' "
    mathfemale="select  math_score from dataset where gender='female' "
    readmale="select reading_score from dataset where gender='male'  "
    readfemale="select reading_score from dataset where gender='female'  "
    writemale="select writing_score from dataset where gender='male'  "
    writefemale="select writing_score from dataset where gender='female'  "

    # print(sqlquery)
    # print(sqlqueryr)
    # print(sqlqueryp)
    # print(sqlqueryt)
    # print(sqlqueryl)
    # print(sqlquerymath)
    # print(mathmale)
    # print(mathfemale)
    # print(sqlqueryread)
    # print(sqlquerywrite)
    # print(readmale)
    # print(readfemale)
    # print(writemale)
    # print(writefemale)

    cursor = connection.cursor()
    
    cursor.execute(sqlquery)
    data=cursor.fetchall()
    # print(data) 
    female=data[0][0]
    male=data[1][0]
    
    cursor.execute(sqlqueryr)
    data=cursor.fetchall()
    # print(data)
    groupA=data[0][0]
    groupB=data[1][0]
    groupC=data[2][0]
    groupD=data[3][0]
    groupE=data[4][0]
    
    cursor.execute(sqlqueryp)
    data=cursor.fetchall()
    # print(data)
    associate=data[0][0]
    bachelor=data[1][0]
    high=data[1][0]
    master=data[2][0]
    some=data[3][0]
    someh=data[4][0]
    
    cursor.execute(sqlqueryt)
    data=cursor.fetchall()
    # print(data)
    completed=data[0][0]
    nones=data[1][0]
    
    
    cursor.execute(sqlqueryl)
    data=cursor.fetchall()
    # print(data)
    free=data[0][0]
    standard=data[1][0]
    
    cursor.execute(sqlquerymath)
    data=cursor.fetchall()
    # print('mathdata')
    maths = [item[0] for item in data]
    # print(maths)
    # print('maths frequency')
    freq_math = [[num,maths.count(num)] for num in set(maths)]
    # print(freq_math)

    
    cursor.execute(mathmale)
    data=cursor.fetchall()
    # print('math male')
    mathm = [item[0] for item in data]
    # print(mathm)
    
    cursor.execute(mathfemale)
    data=cursor.fetchall()
    # print('math female')
    mathf = [item[0] for item in data]
    # print(mathf)
    
    cursor.execute(sqlqueryread)
    data=cursor.fetchall()
    # print('read data')
    read = [item[0] for item in data]
    # print(read)
    # print('read frequency')
    freq_read = [[num,read.count(num)] for num in set(read)]
    # print(freq_read)

    cursor.execute(readmale)
    data=cursor.fetchall()
    # print('read male')
    readm = [item[0] for item in data]
    # print(readm)
    
    cursor.execute(readfemale)
    data=cursor.fetchall()
    # print('read female')
    readf = [item[0] for item in data]
    # print(readf)
    
    cursor.execute(sqlquerywrite)
    data=cursor.fetchall()
    # print('write data')
    write = [item[0] for item in data]
    # print(write)
    # print('write frequency')
    freq_write = [[num,write.count(num)] for num in set(write)]
    # print(freq_write)

    cursor.execute(writemale)
    data=cursor.fetchall()
    # print('write male')
    writem = [item[0] for item in data]
    # print(writem)
    
    cursor.execute(writefemale)
    data=cursor.fetchall()
    # print('write female')
    writef = [item[0] for item in data]
    # print(writef)
    connection.close()
    cursor.close()
    print(data[0][0])
    
    # Assuming you have variables like female, male, groupA, ..., freq_write
    data_dict = {
    'female': female,
    'male': male,
    'groupA': groupA,
    'groupB': groupB,
    'groupC': groupC,
    'groupD': groupD,
    'groupE': groupE,
    'bachelor': bachelor,
    'some': some,
    'someh': someh,
    'associate': associate,
    'master': master,
    'high': high,
    'nones': nones,
    'completed': completed,
    'standard': standard,
    'free': free,
    'maths': maths,
    'mathm': mathm,
    'mathf': mathf,
    'read': read,
    'readm': readm,
    'readf': readf,
    'write': write,
    'writem': writem,
    'writef': writef,
    'freq_math': freq_math,
    'freq_read': freq_read,
    'freq_write': freq_write,
    }

    # Unpack the dictionary into the render_template call
    return render_template('dashboard.html', **data_dict)

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/predict',methods=['GET','POST'])   
def predict():
    gen = request.args['gender']
    print("gender",gen,'type',type(gen))
    parent = request.args['parentEducation']
    print("parent",parent,'type',type(parent))
    race = request.args['race']
    print("race",race,'type',type(race))
    lunch = request.args['lunch']
    print("lunch",lunch,'type',type(lunch))
    test = request.args['testPrep']
    print("test",test,'type',type(test))
        # Prepare input data for prediction
    input_data = pd.DataFrame({
    'gender': [gen],
    'race/ethnicity': [race],
    'parental level of education': [parent],
    'lunch': [lunch],
    'test preparation course': [test]
    })
    df = pd.read_csv(fn)
    # Extract features and target variables
    X = df.drop(['math score', 'reading score', 'writing score'], axis=1)
    X = pd.get_dummies(X, columns=['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course'])
    y_math = df['math score']
    y_reading = df['reading score']
    y_writing = df['writing score']

    # Split the dataset into training and testing sets
    X_train_math, X_test_math, y_train_math, y_test_math = train_test_split(X, y_math, test_size=0.02, random_state=42)
    X_train_reading, X_test_reading, y_train_reading, y_test_reading = train_test_split(X, y_reading, test_size=0.02, random_state=42)
    X_train_writing, X_test_writing, y_train_writing, y_test_writing = train_test_split(X, y_writing, test_size=0.02, random_state=42)

    # Create linear regression models
    model_math = LinearRegression()
    model_reading = LinearRegression()
    model_writing = LinearRegression()

    # Train the models on the training data
    model_math.fit(X_train_math, y_train_math)
    model_reading.fit(X_train_reading, y_train_reading)
    model_writing.fit(X_train_writing, y_train_writing)

    # Convert categorical input into numerical using one-hot encoding
    input_data = pd.get_dummies(input_data, columns=['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course'])

    # Align input_data columns with the columns in training data
    input_data = input_data.reindex(columns=X.columns, fill_value=0)
    print(input_data)
    # Predict scores
    math_score_pred = model_math.predict(input_data)
    reading_score_pred = model_reading.predict(input_data)
    writing_score_pred = model_writing.predict(input_data)

    print(f'Predicted Math Score: {math_score_pred[0]:.2f}')
    print(f'Predicted Reading Score: {reading_score_pred[0]:.2f}')
    print(f'Predicted Writing Score: {writing_score_pred[0]:.2f}')

    msg = {
    "math_score": math_score_pred[0],
    "reading_score": reading_score_pred[0],
    "writing_score": writing_score_pred[0]
    }
    result = make_response(json.dumps(msg))
    print(msg, flush=True)
    return result


@app.route('/dataloader')
def dataloader():
    return render_template('dataloader.html')

@app.route('/savedataset', methods = ['POST'])
def savedataset():
    print("request :"+str(request), flush=True)
    if request.method == 'POST':
        # connection = mysql.connector.connect(host='localhost',database='student_db',user='root',password='')
        # cursor = connection.cursor()
    
        prod_mas = request.files['dt_file']
        filename = secure_filename(prod_mas.filename)
        prod_mas.save(os.path.join("./static/uploads/", filename))

        #csv reader
        fn = os.path.join("./static/Uploads/", filename)
        savedata(fn)
        return render_template('dataloader.html',data="Data loaded successfully")

    
@app.route('/cleardataset', methods = ['POST'])
def cleardataset():
    print("request :"+str(request), flush=True)
    if request.method == 'POST':
        connection = mysql.connector.connect(host='localhost',database='student_db',user='root',password='')
        sqlquery="delete from dataset"
        print(sqlquery)
        cursor = connection.cursor()
        cursor.execute(sqlquery)
        connection.commit() 
        connection.close()
        cursor.close()
        return render_template('dataloader.html',data="Data cleared successfully")
   


@app.route('/planning')
def planning():
    return render_template('planning.html')

@app.route('/plan',methods=['GET','POST'])
def plan():
    gen = request.args['gender']
    print("gender",gen,'type',type(gen))
    parent = request.args['parentEducation']
    print("parent",parent,'type',type(parent))
    race = request.args['race']
    print("race",race,'type',type(race))
    
    connection=mysql.connector.connect(host='localhost',database='student_db',user='root',password='')
    cursor=connection.cursor()
    lunchs = ('select math_score, reading_score, writing_score from dataset where gender="' + gen + '" and race="' + race + '" and parental="'+parent+'" and lunch="standard" and test_prep="completed"')

    lunchf = ('select math_score, reading_score, writing_score from dataset where gender="' + gen + '" and race="' + race + '" and parental="'+parent+'" and lunch="free/reduced" and test_prep="none"')

    testc = ('select math_score, reading_score, writing_score from dataset where gender="' + gen + '" and race="' + race + '" and parental="'+parent+'" and lunch="free/reduced" and test_prep="completed"')

    testf = ('select math_score, reading_score, writing_score from dataset where gender="' + gen + '" and race="' + race + '" and parental="'+parent+'" and lunch="standard" and test_prep="none"')

    # ...
    # print(lunchs)   
    # print(lunchf)
    # print(testc)
    # print(testf)

    cursor.execute(lunchs)
    data = cursor.fetchall()

    cursor.execute(lunchf)
    data1 = cursor.fetchall()

    cursor.execute(testc)
    data2 = cursor.fetchall()

    cursor.execute(testf)
    data3 = cursor.fetchall()

    # print(lunchs)
    # print(lunchf)
    # print(testc)
    # print(testf)
    print(data)
    print(data1)
    print(data2)
    print(data3)
    connection.close()
    cursor.close()
    data_dict = {
    'standc': data,
    'freen': data1,
    'freec': data2,
    'standn': data3,
    }
    resp =make_response(json.dumps(data_dict))
    return resp

if __name__ == '__main__':
    app.run(debug=True)