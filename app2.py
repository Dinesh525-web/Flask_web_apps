from flask import Flask, request, render_template
from datetime import date

#### Defining Flask App
app = Flask(__name__)

#### Saving Date today in 2 different formats
datetoday = date.today().strftime("%m_%d_%y")
datetoday2 = date.today().strftime("%d-%B-%Y")

def replace_multiple_newlines(text):
    lines = text.split('\n')
    lines = [line for line in lines if line.strip()]
    return len(lines)

################## ROUTING FUNCTIONS #########################

#### Our main page
@app.route('/')
def home():
    return render_template('home2.html', datetoday2=datetoday2) 

#### This function will run when we submit the form
@app.route('/count', methods=['POST'])
def count():
    text = request.form.get('text', '')  # Use .get() to avoid KeyError
    
    words = len(text.split())
    
    paras = replace_multiple_newlines(text)

    text = text.replace('\r', '')
    text = text.replace('\n', '')

    chars = len(text)
    return render_template('home2.html', words=words, paras=paras, chars=chars, datetoday2=datetoday2) 

#### Our main function which runs the Flask App
if __name__ == '__main__':
    app.run(debug=True)
