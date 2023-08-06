from flask import *
import json
from cs200.main import Controller
import secrets

app = Flask(__name__)

##
##def verify(token):
##    
##    for tok in tokens:
##        if tok == token:
##            return True
##
##    # If none of the tokens are authentic, return false value by default
##    return False

@app.route("/")
@app.route("/homepage")
def home():
    return send_file("./public/index.html")

@app.route("/search/<query>/token=<token>")
def search(query, token):
    
    #verify_token = verify(token)

    if verify_token:
        ctrl = Controller()
    
        return str(ctrl.return_summarization(concept = query))
    
    else:
        return "Token not appropriate for task."
    
if __name__ == "__main__":

    with open("config/options.json") as jsn:
        info = json.loads(jsn.read())
        
    app.run(port=info["PORT"])
    
