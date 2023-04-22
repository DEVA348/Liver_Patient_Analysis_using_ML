from flask import Flask,render_template,request
import numpy as np
import pickle
app=Flask(__name__,template_folder = 'template')
@app.route('/')
def base():
  return render_template('base.html')
@app.route('/Home')
def home():
  return render_template('home.html')
@app.route('/About')
def about():
  return render_template('about.html')
@app.route('/predict')
def index():
 return render_template("liverprediction.html")

@app.route('/data_predict',methods = ['POST'])
def predict():
    age = request.form['age']
    gender=request.form['gender']
    tb=request.form['tb']
    db=request.form['db']
    ap=request.form['ap']
    aa1=request.form['aa1']
    aa2=request.form['aa2']
    tp=request.form['tp']
    a=request.form['a']
    agr=request.form['agr']
    data = [[float(age),float(gender),float(db),float(ap),float(aa1),float(aa2),float(tp),float(a),float(agr)]]
    model = pickle.load(open('ETC.pkl','rb'))
    prediction = model.predict(data)[0]
    if(prediction==1) :
      return render_template('noChance.html',prediction='You have a liver desease problem,You must and should consult a doctor.Take care')
    else:
      return render_template('chance.html', prediction='You dont have a liver desease problem')

if __name__=='__main__' :
  app.debug= True
  app.run()
