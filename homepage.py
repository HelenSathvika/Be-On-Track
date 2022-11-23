#! /usr/bin/python3
import psycopg2
import sample
from flask import Flask,render_template
app=Flask(__name__)

'''
For Connecting Database
'''
 
def get_db_connection():    
    conn=psycopg2.connect(host='localhost',database='postgres',user='postgres',password='pavani',port='5432')
    return conn
 
'''
For rendering Homepage
'''   
@app.route('/')
def home():
    return render_template('project.html')

'''
   For rendering interviewbit
   '''
@app.route('/interviewbit',methods=['POST'])
def interviewbit():

     conn=get_db_connection()
     cur=conn.cursor()
     cur.execute('SELECT * FROM interviewbit;')
     x=cur.fetchall()
     return render_template('interviewbit.html',output1=x)


'''
For rendering hackerearth
'''
@app.route('/hackerearth',methods=['POST'])
def hackerearth():
 
     conn=get_db_connection()
     cur=conn.cursor()
     cur.execute('SELECT * FROM hackerearth;')
     x=cur.fetchall()
     return render_template('hackerearth.html',output2=x)

'''
 For rendering leetcode
 '''
@app.route('/leetcode',methods=['POST'])
def leetcode():

     conn=get_db_connection()
     cur=conn.cursor()
     cur.execute('SELECT * FROM leetcode;')
     x=cur.fetchall()
     return render_template('leetcode.html',output3=x)
 
'''
For rendering atcoder
'''    
@app.route('/atcoder',methods=['POST'])
def atcoder():
 
     conn=get_db_connection()
     cur=conn.cursor()
     cur.execute('SELECT * FROM atcoder;')
     x=cur.fetchall()
     return render_template('atcoder.html',output4=x)

'''
For rendering toph
'''
@app.route('/toph',methods=['POST'])
def toph():
 
     conn=get_db_connection()
     cur=conn.cursor()
     cur.execute('SELECT * FROM toph;')
     x=cur.fetchall()
     return render_template('toph.html',output5=x)
'''
 For rendering icpc
 '''
@app.route('/icpc',methods=['POST'])
def icpc():

     conn=get_db_connection()
     cur=conn.cursor()
     cur.execute('SELECT * FROM icpc;')
     x=cur.fetchall()
     return render_template('icpc.html',output6=x)

'''
 For rendering hackerearth1
 '''
@app.route('/hackerearth1',methods=['POST'])
def hackerearth1():

     conn=get_db_connection()
     cur=conn.cursor()
     cur.execute('SELECT * FROM hackerearth1;')
     x=cur.fetchall()
     return render_template('hackerearth1.html',output7=x)

'''
For rendering spoj
'''
@app.route('/spoj',methods=['POST'])
def spoj():
 
     conn=get_db_connection()
     cur=conn.cursor()
     cur.execute('SELECT * FROM spoj;')
     x=cur.fetchall()
     return render_template('spoj.html',output8=x)
if __name__ == "__main__":
 app.run(host='127.0.0.0',port='5000')
