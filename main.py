from flask import Flask, request 

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
        <h1>Hello Flask</h1>
        <p>Revisit and successful test of installation and setup of flask environment</p>
        <p> Adding and testing a Post action with the FORM below </p>
        <form action="/hello" method="post">
            <label for="first-name">First Name:</label>
            <input id="first-name" type="text" name="first_name" />
            <input type="submit" />
        </form>
        <a href="/next">What's next?</a>
    </body>
</html>
"""

docuNext = """
<!doctype html>
<html>
    <head>
        <title>What's coming next?</title>
    </head>
    <body>
        <p>Next I will attempt to integrate a templating engine. Wish me luck please.</p>
    </body>
</html>"""

@app.route("/")
def index():
    return form

@app.route("/next", methods=['GET'])
def next():
    return docuNext    

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h2>The post request was successful : <span style="color:blue">' + first_name + '</span></b></h2>'

app.run()