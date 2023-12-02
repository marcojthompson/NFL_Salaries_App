from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', message = 'Hello, World!')

@app.route('/process_form', methods = ["POST"])
def process_form():
    team = request.form.get('team_choice')
    return redirect(url_for('show_team_page', team_choice = team))

@app.route('/team/<team_choice>')
def show_team_page(team_choice):
    return render_template('team.html', team = team_choice)

if __name__ == '__main__':
    app.run(debug = True)
