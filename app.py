from flask import Flask, render_template, redirect, url_for,request, session, flash


app = Flask(__name__)

#-----------------------MAIN MAP PAGE--------------------------
@app.route("/", methods = ['GET', 'POST'])
def root():
    return render_template("index.html")


#---------------------ONE STATE-------------------------------
@app.route("/<id>", methods = ['GET', 'POST'])
def state_graphs(id):
    if id == "NY":
        return "hi"

@app.route("/compare/", methods = ['GET', 'POST'])
def compare():
    state1 = request.args['state1']
    state2 = request.args['state2']
    return state1 + " " + state2

if __name__ == "__main__":
    app.run(debug=True)
