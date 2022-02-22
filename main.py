from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')



# def base():
#     name = "Tanner"
#     return render_template('base.html', name = name)

# @app.route('/home')
# def home():
#     return render_template('home.html')

# @app.route('/index')
# def index():
#     return render_template('index.html')

# dynamic routing
# @app.route('/user/<username>')
# def user(username):
#     return f"This is the home page for {username.upper()}"








if __name__ == '__main__':
    app.run(debug=True)