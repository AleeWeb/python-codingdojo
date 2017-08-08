from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def greeting():
    return render_template('index.html', greeting="Welcome")
app.run(debug=True)

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', info="The ninja was a covert agent in feudal Japanese times who specialized in unorthodox warfare including espionage, sabotage, infiltration, and assassination. Compared to the samurai who were very upfront and honorable with their tactics, the ninja proved a stark contrast.")
app.run(debug=True)