import psycopg2
import sample
from flask import Flask, request, jsonify, render_template
from joblib import load
app=Flask(__name__) 
exec('sample')
def get_db_connection():    
 conn=psycopg2.connect(host='localhost',database='postgres',user='postgres',password='pavani',port='5432')
 return conn
@app.route('/')
def home():
 return render_template('project.html')

@app.route('/interviewbit',methods=['POST'])
def interviewbit():
 '''
 For rendering interviewbit
 '''
 conn=get_db_connection()
 cur=conn.cursor()
 cur.execute('SELECT * FROM interviewbit;')
 x=cur.fetchall()
 cur.close()
 return render_template('index.html')

@app.route('/hackerearth',methods=['POST'])
def hackerearth():
 '''
 For rendering interviewbit
 '''
 conn=get_db_connection()
 cur=conn.cursor()
 cur.execute('SELECT * FROM hackerearth;')
 x=cur.fetchall()
 cur.close()
 return render_template('index.html')

@app.route('/leetcode',methods=['POST'])
def leetcode():
 '''
 For rendering interviewbit
 '''
 conn=get_db_connection()
 cur=conn.cursor()
 cur.execute('SELECT * FROM leetcode;')
 x=cur.fetchall()
 cur.close()
 return render_template('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1',port='5000')
