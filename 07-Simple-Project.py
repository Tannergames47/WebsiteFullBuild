# Set up your imports and your flask app.
from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def test():
    return render_template('test.html')
    # This home page should have the form.
    


# This page will be the page after the form
@app.route('/report')
def report():
    lower_letter = False
    upper_letter = False
    end_number = False

    username = request.args.get('username')


    lower_letter = any(i.islower() for i in username)
    upper_letter = any(i.isupper() for i in username)
    end_number = username[-1].isdigit()

    #Check if all are True
    report = lower_letter and upper_letter and end_number

    return render_template('report.html',report=report,
                           lower=lower_letter,upper=upper_letter,
                           end_number=end_number)
    

if __name__ == '__main__':
    app.run(debug=True)



