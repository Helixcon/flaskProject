from flask import Flask, render_template, request

import math

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello, Flask!"


@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    if request.method == 'POST':
        try:
            # Get the form data from the request
            height_feet = float(request.form['height_feet'])
            height_inches = float(request.form['height_inches'])
            weight_pounds = float(request.form['weight_pounds'])

            # Convert height to inches
            height_in = (height_feet * 12) + height_inches

            # Calculate BMI
            bmi = calculate_bmi(height_in, weight_pounds)

            # Get BMI category
            bmi_category = get_bmi_category(bmi)

            # Render the results template with the calculated BMI and BMI category
            return render_template('results.html', bmi=bmi, bmi_category=bmi_category)
        except Exception as e:
            return render_template('error.html', message=str(e))
    # If the request method is not POST, render the BMI calculator template
    else:
        return render_template('bmi.html')


def calculate_bmi(height_in, weight_pounds):
    try:
        bmi = (weight_pounds * 703) / math.pow(height_in, 2)
        bmi_rounded = round(bmi, 1)
        return bmi_rounded
    except Exception as e:
        return str(e)


def get_bmi_category(bmi):
    try:
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 24.9:
            return "Normal"
        elif bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"
    except Exception as e:
        return str(e)
