from flask import Flask, render_template, redirect, url_for,request, session, flash


app = Flask(__name__)

#-----------------------MAIN MAP PAGE--------------------------
@app.route("/", methods = ['GET', 'POST'])
def root():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
