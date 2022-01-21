
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/<string:name>')
def dynamic_route(name):
    return render_template(name)

def add_to_database(email, subject, body):
    with open('database.txt', mode='a') as database:
        data = database.write(f"\n{email},{subject},{body}")


@app.route('/email', methods=["POST"])
def login():
    if request.method == "POST":
        data = request.form.to_dict()
        email = data["email"]
        name = email.split("@")
        subject = data["subject"]
        body = data["text"]

        add_to_database(email, subject, body)
    
    return render_template('thankyou.html', name=name[0])

@app.route('/favicon.ico')
def favicon():
    return "bye"
# app.add_url_rule('/favicon.ico',
#                  redirect_to=url_for('static', filename='favicon.ico'))

if __name__ == '__main__':
    app.run(debug=True)