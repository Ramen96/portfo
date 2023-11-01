from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/") # routes to home page
def home():
    return render_template('index.html')

@app.route("/<path>") # routes to any sub directory
def route(path):
		return render_template(path)


# def write_to_file(data):
# 	with open("C:/Web_Server/database.txt", mode='a') as database:
# 		email = data['email']
# 		subject = data["subject"]
# 		message = data["message"]
# 		file = database.write(f"{email}, {subject}, {message}")


def write_to_csv(data):
	with open("C:/Web_Server/database.csv", mode='a', newline='') as database2:
		message = data["message"]
		subject = data["subject"]
		email = data['email']
		csv_writer = csv.writer(database2, delimiter=',', quotechar= '"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow({email, subject, message})



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'did not save to database'
	else:
		return "somthing went wrong try again."
