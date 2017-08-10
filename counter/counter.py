from flask import Flask, render_template
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
app.count = 0

@app.route('/')
def count():
    session['count'] += 1
    return render_template('counter.html', count=session['count'])

@app.route('/increment', methods=['POST'])
def increment():
    session['count'] += 1
    #We only increment by 1 since reloading the page also increments
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)