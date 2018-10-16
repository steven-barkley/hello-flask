from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return "<h1>"+"Hello Flask"+"</h1><p>"+"Revisit and successful test of installation and setup of flask environment"+"</p>"
    

app.run()