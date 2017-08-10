from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'appKey'

@app.route('/')
def surveyOptions():
    optionList = ['D.C.', 'Chicago', 'San Jose', 'New York', 'Seattle']
    langList = ['JavaScript', 'Python', 'Java', 'PHP']
    return render_template('survey.html', optionList=optionList, langList=langList)

@app.route('/create', methods=['POST'])
def createUser():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/process')

@app.route('/process')
def showUser():
    return render_template('results.html')

app.run(debug=True)