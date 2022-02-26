from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    user_logged_in = False
    name = 'Tanner'
    return render_template('index.html', name=name, user_logged_in=user_logged_in)

@app.route('/location/<loc_name>')
def locaiton(loc_name):
    return render_template('location.html', loc_name=loc_name)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/report')
def report():
    lower_letter = False
    upper_letter = False
    end_number = False

    username = request.args.get('username')

    lower_letter = any(i.islower() for i in username)
    upper_letter = any(i.isupper() for i in username)
    end_number = username[-1].isdigit()

    report = lower_letter and upper_letter and end_number

    return render_template('report.html', report=report,lower=lower_letter,upper=upper_letter, end_number=end_number)

@app.route('/thankyou')
def thankyou():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thankyou.html', first=first, last=last)

@app.route('/about')
def about():
    name = 'Tanner'
    letters = list(name)
    seasons = ['Summer', 'Fall', 'Winter', 'Spring']
    return render_template('about.html', name=name, letters = letters, seasons = seasons)




if __name__ == '__main__':
    app.run(debug=True)