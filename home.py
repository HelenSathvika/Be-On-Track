#! /usr/bin/python3
import psycopg2
import sample
from flask import Flask, request, jsonify, render_template
from joblib import load
app=Flask(__name__)
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
 return render_template('interviewbit.html',output1=x)

@app.route('/hackerearth',methods=['POST'])
def hackerearth():
 '''
 For rendering interviewbit
 '''
 conn=get_db_connection()
 cur=conn.cursor()
 cur.execute('SELECT * FROM hackerearth;')
 x=cur.fetchall()
 return render_template('hackerearth.html',output2=x)

@app.route('/leetcode',methods=['POST'])
def leetcode():
 '''
 For rendering interviewbit
 '''
 conn=get_db_connection()
 cur=conn.cursor()
 cur.execute('SELECT * FROM leetcode;')
 x=cur.fetchall()
 return render_template('leetcode.html',output3=x)
@app.route('/atcoder',methods=['POST'])
def atcoder():
 '''
 For rendering interviewbit
 '''
 conn=get_db_connection()
 cur=conn.cursor()
 cur.execute('SELECT * FROM atcoder;')
 x=cur.fetchall()
 return render_template('atcoder.html',output4=x)
if __name__ == "__main__":
 app.run(host='127.0.0.0',port='5000')
