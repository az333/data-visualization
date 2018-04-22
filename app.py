from flask import Flask, render_template, redirect, url_for,request, session, flash
import json

app = Flask(__name__)

#-----------------------DATA PARSING--------------------------
def parseData():
    inFile = open('./data/data.csv', 'rU')
    dataStr = inFile.read()
    statesStr = dataStr.split('\n\n')
    data = dict()

    for state in statesStr:
        stateData = dict()
        stateData['causes'] = []

        lines = state.split('\n')
        causes = lines[1:11]

        for cause in causes:
            entries = cause.split(';')

            #name
            entries[0] = entries[0][entries[0].find(' ')+1:]

            #deaths
            entries[1] = int(entries[1].replace(',', ''))

            #rate
            entries[2] = float(entries[2])

            #rank
            entries[3] = int(entries[3].replace(' (tie)', '')[:-2])

            #us rate
            entries[4] = float(entries[4])

            stateData["causes"].append(entries)

        abbrev = state[0:2]
        data[str(abbrev)] = stateData

    return data

data = parseData()
causes=data["NY"]['causes'][0][0]
print causes
print data.keys()
#-----------------------MAIN MAP PAGE--------------------------
@app.route("/", methods = ['GET', 'POST'])
def root():
    return render_template("index.html")


#---------------------ONE STATE-------------------------------
@app.route("/<stateId>", methods = ['GET', 'POST'])
def state_graphs(stateId):
    return render_template('state.html', state=stateId, causes=data[str(stateId)]['causes'])

@app.route("/compare/", methods = ['GET', 'POST'])
def compare():
    state1 = request.args['state1']
    state2 = request.args['state2']
    return render_template('compare.html', state1=state1,state2=state2, causes1 = data[str(state1)]['causes'], causes2 = data[str(state2)]['causes'])

if __name__ == "__main__":
    app.run(debug=True)
