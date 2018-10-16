from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return "<h1>"+"Hello Flask"+"</h1>" + "</br>" +
            "<p> A revisit of how to install and run a flask app.</p>" +
            "<p> This exercise was extremely educational." 

app.run()