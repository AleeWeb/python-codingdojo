from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def greeting():
    return render_template('index.html', greeting="Welcome")
 

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', info="The ninja was a covert agent in feudal Japanese times who specialized in unorthodox warfare including espionage, sabotage, infiltration, and assassination.")

@app.route('/dojos/new')
def form():
    return render_template('dojos.html', form="Field")

app.run(debug=True)