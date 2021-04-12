from flask import Flask, render_template, request
import pickle
import numpy as np
import random, threading, webbrowser
import os

app = Flask(__name__)

mod = pickle.load(open('Titanic_model', 'rb'))
ag = pickle.load(open('Age_model', 'rb'))

@app.route('/')
def home():
    return render_template('main.html')


@app.route('/predict', methods=['POST'])
def predict():
    val = [x for x in request.form.values()]
    
    name = val[1]+' '+val[2]
    if len(name)<2:
        name = 'Unknown'
    
    title = val[0]
    if 'Mr.' in title:
        title = 1
    elif 'Mrs.' in title:
        title = 2
    elif 'Miss'in title:
        title = 0
    else:
        title = 3
    
    fare = val[3]
    try :
        fare = int(fare)
    except :
        fare = 35
    
    fare = int(np.sqrt(fare))
    if fare>13:
        fare = 13
        
    clss = val[4]
    if 'First' in clss:
        clss = 1
    elif 'Second' in clss:
        clss = 2
    else:
        clss = 3
        
    sex = val[6]
    if 'fe' in sex:
        sex = 0
    else:
        sex = 1
    
    sb = val[7]
    try :
        sb = int(sb)
    except :
        sb = 0
    
    pa = val[8]
    try :
        pa = int(pa)
    except :
        pa = 0
    
    em = val[9]
    if 'C' in em:
        em = 0
    elif 'Q' in em:
        em = 1
    else:
        em = 2
        
    family = sb + pa + 1
    
    alone = 0
    if family==1:
        alone = 1
    
    age = val[5]
    try :
        age = int(age)
    except :
        age = ag.predict([[clss, sex, sb, pa, fare, em, title, family, alone]])
        age = int(age)
    
    val2 = [title, fare, clss, age, sex, sb, pa, em, family, alone, ]
    
    t = ['Mr.', 'Mrs.', 'Miss', 'Unkown']
    titles = []
    for i in range(0,len(t)):
        if val[0] in t[i]:
            ti = 1
        else:
            ti=0
        titles.append(ti)
    
    features = titles + [fare, clss, age, family, sex, sb, alone, pa, em]
    
    survived = mod.predict([features])
    if survived==1:
        txt = f'Great News!!!'
        txt2= f'Passenger {val[0]} {name}, age-{age}'
        txt3= f'Traveling in {val[4]} class and Embarked at {val[9]} is Survived.'
        return render_template('survived.html', txt=txt, txt2=txt2, txt3=txt3)
    else:
        txt = f'Bad News'
        txt2= f'Passenger {val[0]} {name}, age-{age}'
        txt3= f'Traveling in {val[4]} class and Embarked at {val[9]} didn't Survived.'
        txt4= f'RIP {val[0]} {name}'
        return render_template('not-survived.html', txt=txt, txt2=txt2, txt3=txt3, txt4=txt4)
    
if __name__ == "__main__":
    port = 5000 + random.randint(0, 999)
    url = "http://127.0.0.1:{0}".format(port)
    threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    app.run(port=port, debug=False)
