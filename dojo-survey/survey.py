from Flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def something():
    return render_template('survey.html', blank="welcome")