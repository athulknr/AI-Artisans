from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')  # Adjust if you have a different path

@app.route('/signup')
def signup():
    return render_template('signup.html')  # Adjust if you have a different path

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')  # Adjust if you have a different path

@app.route('/our_team')
def our_team():
    return render_template('our_team.html')  # Adjust if you have a different path

if __name__ == '__main__':
    app.run(debug=True)
