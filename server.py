from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/<page_link>')
def my_home(page_link=None):
    return render_template(page_link)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'failure saving to database'
    else:
        '404 error!'


def write_to_file(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.txt', 'a') as db:
        db.write(f"{email},{subject},{message}\n")


def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv', 'a', newline='') as csvdb:
        csv_writer = csv.writer(csvdb, delimiter=",", quotechar='`', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
